from django import forms
from django.core.exceptions import ValidationError

from sitio.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'blood_type', 'liters_required', 'location','body', 'photo', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
