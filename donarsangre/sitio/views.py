from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from sitio.forms import PostForm
from sitio.models import Post, Location, BloodType
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
            photo = request.FILES.get('photo', False)
            if not photo:
                nueva.photo = None
            else:
                nueva.photo = photo
            nueva.author = request.user
            nueva.save()
            return redirect("/inicio/")
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def post_list(request): #Muestra todas las publicaciones no vencidas.
    posteos = Post.objects.filter(expiration_date__gte=datetime.now()).order_by("expiration_date")
    localidades = Location.objects.all()
    tipos = BloodType.objects.all()

    localidad = request.GET.get('localidad')
    factorGrupo = request.GET.get('factorGrupo')
    fechaDesde = request.GET.get('fechaDesde')
    fechaHasta = request.GET.get('fechaHasta')

    if localidad:
        posteos = posteos.filter(location__nombre = localidad)

    if factorGrupo:
        posteos = posteos.filter(blood_type__blood_type = factorGrupo)

    if fechaDesde:
        posteos = posteos.filter(expiration_date__gte = fechaDesde)

    if fechaHasta:
        posteos = posteos.filter(expiration_date__lte = fechaHasta)

    return render(request, 'inicio.html', {'lista_posteos': posteos, 'localidades' : localidades, 'factores_grupos' : tipos })

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
