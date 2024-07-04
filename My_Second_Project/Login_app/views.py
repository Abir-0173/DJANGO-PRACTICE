from django.shortcuts import render
from Login_app.forms import UserForm, UserInfoForm

# Create your views here.

def index(request):
    dict = {}
    return render(request, 'Login_app/index.html', context=dict)



def register(request):

    registerd = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pics' in request.FILES:
                user_info.profile_pics = request.FILES['profile_pics']
                
            user_info.save()

            registerd = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()
    user_form = UserForm()
    user_info_form = UserInfoForm()
    dict = {'user_form': user_form, 'user_info_form': user_info_form, 'registerd':registerd,}
    return render(request, 'Login_app/register.html', context=dict)