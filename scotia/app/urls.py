from django.urls import path
from .views import ListProviderView

urlpatterns = [
    path('providers/', ListProviderView.as_view(), name="providers-all")
    #path('products/', ListProductView.as_view(), name="products-all")
]
