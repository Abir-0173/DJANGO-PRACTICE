# your_app/urls.py
from django.urls import path
from . import views # calling all views in here

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),  # Define root URL
    path('index/', views.index, name='index'),  # Define root URL
    path('form/', views.form, name='form'), # Define
    path('index_1/', views.index_1, name='index_1'),  
    path('form_1/', views.form_1, name='form_1'),
    # Add other URL patterns here
]


