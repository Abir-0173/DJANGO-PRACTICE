from django import forms
from django.core import validators
# from first_app.models import Album, Musician
from first_app import models
# from django.core.validators import validate_email

class MusicianForm(forms.ModelForm):
    class Meta():
        model = models.Musician
        fields = '__all__'
        # exclude = ['first_name']
        # fields = ['first_name', 'last_name', ]


# def even_or_not(value):
#     if value%2 == 1:
#         raise forms.ValidationError("please Insert an Even Number!")
    
# ===  =================================================================
# class user_form(forms.Form):
#     user_email = forms.CharField()
#     user_vmail = forms.CharField()
#     # number_field = forms.IntegerField(validators=[even_or_not])

#     def clean(self):
#         all_cleaned_data = super().clean()
#         user_email = all_cleaned_data['user_email']
#         user_vmail = all_cleaned_data['user_vmail']

#         if user_email!= user_vmail:
#             raise forms.ValidationError("Email and Verify Email must be same!")


# =================================================================
# class user_form(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    # number_field = forms.IntegerField(validators=[validators.MaxLengthValidator(15), validators.MinLengthValidator(5)])
# =================================================================
# class user_form(forms.Form):
    # boolean_field = forms.BooleanField(required=False)
    # field = forms.CharField(max_length=15, min_length=5)
    # field = forms.ChoiceField(choices=(('', '--SELECT OPTION--'),('1','first'), ('2','second'), ('3','third'), ('4','fourth'), ('5','fifth'), ('6','six')))
    # choices=(('', '--SELECT OPTION--'),('1','first'), ('2','second'), ('3','third'), ('4','fourth'), ('5','fifth'), ('6','six'))
    # field = forms.ChoiceField(choices=choices, required=False)
    # choices = (('', '--SELECT OPTION--'),('A','A'), ('B','B'), ('C','C'))
    # field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    # choices=(('1','first'), ('2','second'), ('3','third'), ('4','fourth'), ('5','fifth'), ('6','six'))
    # field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)


#================================================================
# class user_form(forms.Form):
#     #<lebel for="submit">Full Name</label>
#     #<input type="text" name="user_name" id="user_name">
#     user_name = forms.CharField(label="Full Name", required=True, widget= forms.TextInput(attrs= {'placeholder':'Enter your full name'}))

#     #<lable for="user_email">User Email</label></br>
#     #<input type="email" name="user_email" id="user_email">
#     user_email = forms.EmailField(label="User Email")
#     password = forms.CharField(widget=forms.PasswordInput)

#     #<input type= "date">
#     user_dob = forms.DateField(label="Date of Birth", widget= forms.DateInput(attrs= {'type':'date'}))

#     remember_me = forms.BooleanField(required=False)
#================================================================
