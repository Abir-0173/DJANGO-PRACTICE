# your_app/urls.py
from django.urls import path
from . import views # calling all views in here

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),  # Define root URL
    path('index/', views.index, name='index'),  # Define root URL
    path('form/', views.form, name='form'), # Define
    # Add other URL patterns here
]


