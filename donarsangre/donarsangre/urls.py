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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include


"""from sitio.views import SignUpView"""

urlpatterns = [
    path('register/', views.register, name='register'),
    path('pantalla_intermedia/', views.pantalla_intermedia, name='pantalla_intermedia'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('inicio/', views.post_list, name='home'),
    path('new_post', views.new_post, name='new_post'),
    path('informacion/', views.informacion, name = 'informacion'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name = 'logout'),
    #path("login/", include("django.contrib.auth.urls")),
    path('', views.post_list, name='inicio'),
    path('informacion/login/', auth_views.LoginView.as_view()),
    path("registro/", SignUpView.as_view(), name="registro"),
    path("user_posts/", views.user_posts, name="user_posts"),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('update_progress/<int:pk>/', views.update_progress, name = 'update_progress'),
    path('rebuild_index/', views.rebuild_index),
    path('search/', include('haystack.urls')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
