from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
from django.db.models import Avg

# Create your views here.

def index_1(request):
    musician_list = Musician.objects.order_by('first_name')
    diction={'title': 'Home Page', 'musician_list':musician_list}
    return render(request, 'first_app/index_1.html', context=diction)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name', 'release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction={'title': 'List of albums', 'artist_info': artist_info,'album_list':album_list,'artist_rating':artist_rating}
    return render(request, 'first_app/album_list.html', context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_1(request)
        else:
            print(form.errors)

    diction={'title': 'Add music','musician_form': form}
    return render(request, 'first_app/musician_form.html', context=diction)

def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request)
        else:
            print(form.errors)

    diction={'title': 'Add album', 'album_form': form,}
    return render(request, 'first_app/album_form.html', context=diction)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
        else:
            print(form.errors)
    diction={'edit_form': form,}
    return render(request, 'first_app/edit_artist.html', context=diction)

def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction= {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        
        if form.is_valid():
            form.save(commit=True)
            # return album_list(request, album_id)
            diction.update({'success_text': 'successfully updated!'})
        else:
            print(form.errors)

    diction.update({'edit_form': form})
    diction.update({'album_id':album_id})
    return render(request, 'first_app/edit_album.html', context=diction)

def delete_album(request, album_id):
    album = Album.objects.get(id=album_id).delete()
    diciton={'delete_success':'Album Deleted successfully!'}
    return render(request, 'first_app/delete.html', context=diciton)


def delete_musician(request, artist_id):
    artist = Musician.objects.get(pk=artist_id)
    diction={'delete_success':'Musician Deleted successfully!',}
    return render(request, 'first_app/delete.html', context=diction)

# =================================================================
# def index_1(request):
#     diction={'sample_text': "hello abir this is",}
#     # diction={'sample_text': Album.objects.get(),}
#     return render(request, 'first_app/index_1.html', context=diction)

# def form_1(request):
#     diction={}
#     return render(request, 'first_app/form_1.html', context=diction)


# def index(request):
#     musician_list = Musician.objects.order_by('first_name')
    
#     diction = {'text_1': 'I am learning django', 'musician': musician_list}
#     return render(request, 'first_app/index.html', context=diction)
    # return render(request, 'first_app/index.html', context=diction)

# def index(request):
#     return HttpResponse("<h1>Hello It's a Home page</h1>")
# =================================================================
# def form(request):
#     new_form = forms.MusicianForm()

#     if request.method == 'POST':
#         new_form = forms.MusicianForm(request.POST)
#         if new_form.is_valid():
#             new_form.save(commit=True)
#             return index(request)
#         else:
#             print('Validation Error')
#             print(new_form.errors)

#     diction = {'test_form': new_form, 'heading_1': 'add new Musicician'}
#     return render(request, 'first_app/form.html', context=diction)
# =================================================================
# def form(request):
#     new_form = forms.user_form()
#     diction = {'text_1': 'Hello this is created from django', 'test_form': new_form,}

#     if request.method == 'POST':
#         new_form = forms.user_form(request.POST)
#         diction.update({'test_form':new_form })

#         if new_form.is_valid():
#             diction.update({'field': 'filds matched'})
#             diction.update({'form_submited':'Yes'})
#         else:
#             print('Validation Error')
#             print(new_form.errors)

#     return render(request, 'first_app/form.html', context=diction)
# =================================================================
# def form(request):
#     new_form = forms.user_form()
#     diction = {'text1': 'Hello this is created from django', 'test_form': new_form,}

#     if request.method == 'POST':
#         new_form = forms.user_form(request.POST)
#         if new_form.is_valid():
#             print('Validation Success')
#             print('Name: '+new_form.cleaned_data['user_name'])
#             print('Email: '+new_form.cleaned_data['user_email'])
#             print('Password: '+new_form.cleaned_data['password'])
#             print('Remember Me: '+str(new_form.cleaned_data['remember_me']))
#         else:
#             print('Validation Error')
#             print(new_form.errors)

#     return render(request, 'first_app/form.html', context=diction)
# =================================================================


# def form(request):
#     diction = {}
#     return HttpResponse(request, 'first_app/form.html', context=diction)
    # return HttpResponse("<h1> This is from test.html</h1>")

# def home(request):
#     return HttpResponse("<h1>Hello Its a Home page</h1> <a href='index/'>index</a>  <a href='contact/'>Contact</a>")


# def index(request):
#     return HttpResponse("<h1>It's a index.</h1><a href='/'>home</a>  <a href='/contact/'>Contact</a>")


# def contact(request):
#     return HttpResponse("<h1>Contact page</h1><a href='/'>home</a>  <a href='/index/'>index</a>")