# from django.conf.urls import url
from django.urls import path
from first_app import views


app_name = 'first_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('about/', views.about, name='about'),
]

