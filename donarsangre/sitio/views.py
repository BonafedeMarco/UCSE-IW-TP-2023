from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import authenticate, UserCreationForm,AuthenticationForm, UserChangeForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from sitio.forms import PostForm, CustomUserForm
from sitio.models import Post, Location, BloodType, Profile
from datetime import datetime
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .tokens import account_activation_token
import hashlib, datetime, random
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from datetime import datetime



def inicio(request):
    return render(request, 'inicio.html', {})

@login_required(login_url='login/')
def informacion(request):
    return render(request, 'informacion.html', {})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect("/inicio/")

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/login.html", {'form': form})

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

def pantalla_intermedia(request):
    return render (request, 'pantalla_intermedia.html', {})

def register(request):
    form = CustomUserForm()
    if  request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.is_active = False
            user.save()
            Profile.objects.create(user=user)
            uidb64= urlsafe_base64_encode(force_bytes(user.pk)) # crea el token encodeado
            domain = get_current_site(request).domain
            link= reverse('activate', kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)}) # arma el link de activacion

            activate_url = domain+link # le agrega el dominio al link

            mail_subject = 'Activa tu cuenta'

            message = 'Hola '+ user.username + '! '+\
                'Gracias por registrarte! Activá tu cuenta con el siguiente link:\n' + activate_url

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
            mail_subject, message, to=[to_email]
            )
            email.send(fail_silently=False)

            return redirect('/pantalla_intermedia')
        else:
            form = CustomUserForm(request.POST)
    return render(request, "registration/signup.html", {'form': form})
     # Si existe el usuario
    if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/pantalla_intermedia')


"""def activate(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if not account_activation_token.check_token(user,token):
            return HttpResponseRedirect('login/'+'?message='+'El usuario ya esta activado')

        if user.is_active:
            return HttpResponseRedirect('login/')
        user.is_active=True
        user.save()
        return HttpResponseRedirect('login/')

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    return HttpResponseRedirect('login/')
    """

def activate(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if not account_activation_token.check_token(user,token):
            return HttpResponseRedirect('/login'+'?message='+'El usuario ya esta activado')

        if user.is_active:
            return HttpResponseRedirect('/login')
        user.is_active=True
        user.save()

        # messages.success(request,'La cuenta se activo correctamente')
        return HttpResponseRedirect('/login')

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None


    return HttpResponseRedirect('/login')

def logout(request):
    do_logout(request)
    return redirect("/inicio/")


def update_progress(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.liters_donated = request.liters_donated
            post.save()
            return redirect("/inicio/")
    else:
        form = PostForm(instance=post)
    return render(request, 'update_progress.html', {'form': form, 'post': post})



"""def new_post(request):

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
    """