from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html', {})