from django.urls import path
from Age_guesser.views import HumanAgeAPIView

urlpatterns = [
    path('human-age/', HumanAgeAPIView.as_view(), name='human_age'),
]
