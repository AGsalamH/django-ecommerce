from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.contrib.auth.views import LoginView

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.

class UserRegisterView(CreateView):
    template_name = 'accounts/auth/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'accounts/auth/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True
    