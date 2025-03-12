from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CategoryAPIView, CategoryDetailAPIView,
    ProductAPIView, ProductDetailAPIView,
    ImageAPIView, ImageDetailAPIView
)

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("products/", ProductAPIView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("images/", ImageAPIView.as_view(), name="image-list"),
    path("images/<int:pk>/", ImageDetailAPIView.as_view(), name="image-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
