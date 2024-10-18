from django.urls import path
from pages.views import create_page, get_page, list_page

urlpatterns = [
    path("create", create_page, name="create_page"),
    path("<int:pk>", get_page, name="get_page"),
    path("list", list_page, name="list_page"),
]
