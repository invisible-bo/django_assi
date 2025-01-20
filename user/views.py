from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm  # 커스텀 폼을 가져옴
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'base.html')

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm  # 커스텀 폼 사용
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')

def user_profile_view(request):
    return render(request, 'user/profile.html', {'user': request.user})