# from django.conf.urls import url
from django.urls import path
from first_app import views


app_name = 'first_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetails.as_view(), name='musician_details'),
    # path('about/', views.about, name='about'),
]

