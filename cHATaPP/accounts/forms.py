from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist


# Using django's custom user models and form creation

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'first-name',
                'type' : 'text',
            }
        )
    )
    
    last_name = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'last-name',
                'type' : 'text',
            }
        )
    )
    
    email = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'email',
                'type' : 'email',
            }
        )
    )

    username = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'username',
                'type' : 'text',
            }
        )
    )
    
    password1 = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'password',
                'type' : 'password',
            }
        )
    )
    
    password2 = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'c-password',
                'type' : 'password',
            }
        )
    )

    class Meta:

        model = User
        
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')



class SignInForm(forms.Form):
    
    username_email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'username-email',
                'type' : 'text',
            }
        )
    )

    password = forms.CharField(
        
        widget=forms.TextInput(
        
            attrs={
                'class' : 'form-control form-control-lg group_formcontrol',
                'name' : 'password',
                'type' : 'password',
            }
        
        )
    
    )


    def clean(self):

        username_email = self.cleaned_data.get('username_email')

        password = self.cleaned_data.get('password')

        qs_username = User.objects.filter(username=username_email)

        qs_email = User.objects.filter(username=username_email)

        if qs_username.exists():

            print('Authenticating with username')

            user = authenticate(username=username_email, password=password)

            if user is None:

                raise forms.ValidationError("Invalid login details. Make sure details are correct ")

            return self.cleaned_data

        elif qs_email.exists():

            print('Authenticating with email')

            username = qs_email[0].username

            user = authenticate(username = username, password=password)

            if not user or not user.is_active:

                raise forms.ValidationError("Invalid login details. Make sure details are correct")

            self.cleaned_data
    

    def login(self, request):

        username_email = self.cleaned_data.get('username_email')
        
        password = self.cleaned_data.get('password')
        
        qs = User.objects.filter(username = username_email)
        
        if qs.exists():
        
            username = username_email
        
        else:

            qs = User.objects.filter(email = username_email)
        
            username = qs[0].username
        
        user = authenticate(username = username, password=password)
        
        return user