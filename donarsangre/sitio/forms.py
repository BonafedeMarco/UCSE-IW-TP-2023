from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sitio.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'blood_type', 'liters_required', 'location', 'body', 'photo', 'latitud', 'longitud', 'expiration_date', 'liters_donated']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomUserForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	class Meta:
		model = User
		fields = ('username','email', 'password1', 'password2')
