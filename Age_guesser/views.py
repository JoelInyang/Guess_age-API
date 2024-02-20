from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import AgePrediction
from .serializers import AgePredictionSerializer
import requests




from datetime import datetime

class HumanAgeAPIView(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        if not name:
            return Response({"error": "Name is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check cache
        prediction = cache.get(name)
        if not prediction:
            # Fetch age prediction from Agify API
            response = requests.get(f'https://api.agify.io/?name={name}')
            if response.status_code == 404:
                return Response({"error": "Name not found."}, status=status.HTTP_404_NOT_FOUND)
            elif response.status_code != 200:
                return Response({"error": "Failed to fetch age prediction."}, status=response.status_code)

            # Save prediction to cache
            data = response.json()
            age = data['age']
            # Calculate date of birth based on the current date
            today = datetime.now().date()
            date_of_birth = today.replace(year=today.year - age)
            date_of_birth_str = date_of_birth.isoformat()
            prediction = AgePrediction(name=name, age=age, date_of_birth=date_of_birth_str)
            prediction.save()
            cache.set(name, prediction, timeout=None)  # Store indefinitely (could be set to expire after a certain time)

        serializer = AgePredictionSerializer(prediction)
        return Response(serializer.data)
