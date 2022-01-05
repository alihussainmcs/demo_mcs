from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('home/', home),
    path('register/', register),
    path('about/', about),
    path('contact/', contact),
    path('service/', service),

]
