from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from sitio.forms import PostForm
from sitio.models import Post
from datetime import datetime

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

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            nueva = form.save(commit=False)
            nueva.author = request.user
            nueva.save()
            return redirect("/inicio/")
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def post_list(request): #Muestra todas las publicaciones no vencidas.
    posteos = Post.objects.filter(expiration_date__gte=datetime.now()).order_by("-created_date") #Falta agregar filtro por defecto de que muestre las no vencidas.
    return render(request, 'inicio.html', {'lista_posteos': posteos})

def user_posts(request): #Muestra las publicaciones del usuario logueado.
    posteos = Post.objects.filter(author = request.user).order_by("-created_date")
    return render(request, 'user_posts.html', {'lista_posteos':posteos})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required(login_url='login/')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("/user_posts/")
