from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Provider
from .serializers import ProviderSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_provider(name="", expiration=""):
        if name != "" and expiration != "":
            Provider.objects.create(name=name, expiration=expiration)

    def setUp(self):
        # add test data
        self.create_provider("like glue", "sean paul")
        self.create_provider("simple song", "konshens")
        self.create_provider("love is wicked", "brick and lace")
        self.create_provider("jam rock", "damien marley")


class GetAllProviderTest(BaseViewTest):

    def test_get_all_providers(self):
        """
        This test ensures that all Provider added in the setUp method
        exist when we make a GET request to the Provider/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("providers-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Provider.objects.all()
        serialized = ProviderSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
