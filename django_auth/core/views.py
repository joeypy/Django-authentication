from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, authenticate, login as do_login
# from .forms import UserCreationFormCustom, LoginFormCustom


############
#   Home   #
############
def home(request):
    User = get_user_model()
    count = User.objects.count()
    return render(request, 'home.html', {
            'count': count
        })


#############
#   Login   #
#############
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, SignUpForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'
    success_url = 'welcome'


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 do_login(request, user)
#                 return redirect('welcome')
#     form = AuthenticationForm()
#     return render(request, "login/login.html", {'form': form})


###############
#   Welcome   #
###############
def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'login/welcome.html')
    return redirect('auth/login')


##############
#   Logout   #
##############
def logout(request):
    do_logout(request)
    return redirect('/')


##############
#   Signup   #
##############
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationFormCustom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('welcome')
#     else:
#         form = UserCreationFormCustom()
#         form.fields['username'].help_text = None
#         form.fields['email'].help_text = None
#         form.fields['password1'].help_text = None
#         form.fields['password2'].help_text = None
#     return render(request, 'registration/signup.html', {
#         'form': form
#     })



