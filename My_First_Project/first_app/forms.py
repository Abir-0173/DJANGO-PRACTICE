from django import forms

class user_form(forms.Form):
    # boolean_field = forms.BooleanField(required=False)
    # field = forms.CharField(max_length=15, min_length=5)
    # field = forms.ChoiceField(choices=(('', '--SELECT OPTION--'),('1','first'), ('2','second'), ('3','third'), ('4','fourth'), ('5','fifth'), ('6','six')))
    # choices=(('', '--SELECT OPTION--'),('1','first'), ('2','second'), ('3','third'), ('4','fourth'), ('5','fifth'), ('6','six'))
    # field = forms.ChoiceField(choices=choices, required=False)
    # choices = (('', '--SELECT OPTION--'),('A','A'), ('B','B'), ('C','C'))
    # field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    choices=(('1','first'), ('2','second'), ('3','third'), ('4','fourth'), ('5','fifth'), ('6','six'))
    field = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)


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
