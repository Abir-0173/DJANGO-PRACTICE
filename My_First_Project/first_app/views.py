from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.
def index_1(request):
    diction={}
    return render(request, 'first_app/index_1.html', context=diction)

def form_1(request):
    diction={}
    return render(request, 'first_app/form_1.html', context=diction)


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    
    diction = {'text_1': 'I am learning django', 'musician': musician_list}
    return render(request, 'first_app/index.html', context=diction)
    # return render(request, 'first_app/index.html', context=diction)

# def index(request):
#     return HttpResponse("<h1>Hello It's a Home page</h1>")
# =================================================================
def form(request):
    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
        else:
            print('Validation Error')
            print(new_form.errors)

    diction = {'test_form': new_form, 'heading_1': 'add new Musicician'}
    return render(request, 'first_app/form.html', context=diction)
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