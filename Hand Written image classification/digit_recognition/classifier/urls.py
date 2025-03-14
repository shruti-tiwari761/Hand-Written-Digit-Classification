from django.urls import path
from .views import classify_digit, draw_page

urlpatterns = [
    path("", draw_page, name="draw_page"),
    path("classify_digit/", classify_digit, name="classify_digit"),
]
