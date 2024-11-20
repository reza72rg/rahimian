from django.urls import path, include
from .views import *

# Set the app name for namespacing
app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name='show_template'),    ]