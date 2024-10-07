"""
Urls for core app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (
    UserViewSet,
    ProductViewSet,
    CategoryViewSet,
    OrderViewSet,
    RegisterAPIView,
    CustomTokenObtainPairView,
    ProfileAPIView,
    ProductFilterViewSet,
    CategoryProductsAPIView,
)

# Create a router and register viewsets with it
router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"orders", OrderViewSet)

# Include the router's URLs into the URL patterns
urlpatterns = [
    path("", include(router.urls)),
    path(
        "category-products/",
        CategoryProductsAPIView.as_view(),
        name="category_products",
    ),
    path(
        "product-filter/",
        ProductFilterViewSet.as_view(),
        name="product_filter",
    ),  # Add this line to your urls.py file to enable filtering by product description.
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
