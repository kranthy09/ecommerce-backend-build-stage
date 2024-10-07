"""
Views
"""

from rest_framework import generics, mixins, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import Product, Category, Order
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    OrderSerializer,
    UserSerializer,
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
    CategoryProductsSerializer,
)


User = get_user_model()


# Register API
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # Allow anyone to access this endpoint


# Login API
class CustomTokenObtainPairView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                serializer.validated_data, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Profile API (Get user profile details)
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductFilterViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]

    def get_queryset(self):
        return Product.objects.all()


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


# Home page API View (Category and its Products)
class CategoryProductsAPIView(APIView):
    """returns response for category and its products"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        queryset = Category.objects.prefetch_related("products")
        serializer = CategoryProductsSerializer(queryset, many=True)
        return Response(serializer.data)
