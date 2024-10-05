# urls.py
from django.urls import path
from .views import PortfolioAPIView

urlpatterns = [
    path('portfolio/', PortfolioAPIView.as_view(), name='portfolio-list'),  # List and create portfolios
    path('portfolio/<int:pk>/', PortfolioAPIView.as_view(), name='portfolio-detail'),  # Retrieve, update, and delete a portfolio
]
