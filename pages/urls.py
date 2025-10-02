from django.urls import path
from .views import home_page_view, AboutPageView, ProductPageView

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("products/", ProductPageView.as_view(), name="products"),
]