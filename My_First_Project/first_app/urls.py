# your_app/urls.py
from django.urls import path
from . import views # calling all views in here

app_name = "first_app"

urlpatterns = [
    path('', views.index_1, name='index_1'),  # Define root URL
    # path('index/', views.index, name='index'),  # Define root URL
    # path('form/', views.form, name='form'), # Define

    path('index_1/', views.index_1, name='index_1'), 
    path('add_album/', views.album_form, name='album_form'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),

    # path('album_list/<int:artist_id/>', views.album_list, name='album_list'),
    # path('form_1/', views.form_1, name='form_1'),
    # Add other URL patterns here
]


