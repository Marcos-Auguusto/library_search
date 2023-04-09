from django.urls import path
from librarySearch.views import home_view

urlpatterns = [
    path("", home_view),
]
