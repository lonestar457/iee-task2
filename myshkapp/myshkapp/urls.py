
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('myshk.urls')),
    path('register/',users_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/',users_views.profile, name='profile'),
    ]