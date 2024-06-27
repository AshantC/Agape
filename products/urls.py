from django.urls import path
from products.views import home_page

urlpatterns = [
    path("", home_page, name="home")
]
