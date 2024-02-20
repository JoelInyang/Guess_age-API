from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import AgePrediction


#Unit Test for Model

class AgePredictionModelTest(TestCase):
    def test_age_prediction_creation(self):
        name = 'test'
        age = 30
        date_of_birth = 1992
        prediction = AgePrediction.objects.create(name=name, age=age, date_of_birth=date_of_birth)

        self.assertEqual(prediction.name, name)
        self.assertEqual(prediction.age, age)
        self.assertEqual(prediction.date_of_birth, date_of_birth)


#Integration Test for API

class HumanAgeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_age_prediction(self):
        url = reverse('human_age')
        data = {'name': 'michael'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'michael')
        self.assertEqual(response.data['age'], 63)
        self.assertEqual(int(response.data['date_of_birth'].split('-')[0]), 1961)


    def test_invalid_name(self):
        url = reverse('human_age')
        data = {'name': 'michael'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'michael')
        self.assertEqual(response.data['age'], 63)
        self.assertEqual(int(response.data['date_of_birth'].split('-')[0]), 1961)



    def test_missing_name(self):
        url = reverse('human_age')
        response = self.client.post(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Name is required.')

