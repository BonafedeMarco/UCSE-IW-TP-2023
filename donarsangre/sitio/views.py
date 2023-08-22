from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio.html', {})

@login_required(login_url='login/')
def informacion(request):
    return render(request, 'informacion.html', {})

def login(request):
    return render(request, 'login.html', {})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"