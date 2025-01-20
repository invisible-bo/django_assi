from django.contrib.auth import views as auth_views 
from django.urls import path
from .views import SignUpView
from .views import user_profile_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_profile_view, name='profile'),
]
