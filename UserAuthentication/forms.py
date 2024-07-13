import django.forms as forms
from UserAuthentication.models import Account 


class UserForm(forms.ModelForm):

    
    class Meta:
        model = Account

        fields = ['username', 'password', 'last_name', 'first_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'password': forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'last_name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'first_name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'maiden_name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'birthday': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline', 'placeholder' : "MM/DD/YYYY"}),
           
        }
        
    


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
            'password': forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline'}),
        }

