"""
URL configuration for donarsangre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sitio import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from sitio.views import SignUpView


"""from sitio.views import SignUpView"""

urlpatterns = [
    path('inicio/', views.post_list),
    path('new_post', views.new_post, name='new_post'),
    path('informacion/', views.informacion, name = 'informacion'),
    path('admin/', admin.site.urls),
    path("login/", include("django.contrib.auth.urls")),
    path('', views.post_list, name='inicio'),
    path('informacion/login/', auth_views.LoginView.as_view()),
    path("registro/", SignUpView.as_view(), name="registro"),
    path("user_posts/", views.user_posts, name="user_posts"),
   
]