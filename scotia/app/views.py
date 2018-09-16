from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Provider
from .serializers import ProviderSerializer


class ListProviderView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
