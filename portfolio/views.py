# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Portfolio, Tag
from .serializers import PortfolioSerializer


class PortfolioAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                portfolio = Portfolio.objects.get(pk=pk)
            except Portfolio.DoesNotExist:
                return Response({"error": "Portfolio not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = PortfolioSerializer(portfolio)
            return Response(serializer.data)
        else:
            portfolios = Portfolio.objects.all()
            serializer = PortfolioSerializer(portfolios, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            return Response({"error": "Portfolio not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            portfolio = Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            return Response({"error": "Portfolio not found"}, status=status.HTTP_404_NOT_FOUND)

        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
