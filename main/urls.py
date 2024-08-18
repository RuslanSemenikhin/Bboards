from django.urls import path
from .views import main_

urlpatterns = [
    path('', main_)
]