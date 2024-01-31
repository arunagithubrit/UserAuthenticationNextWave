from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from Userapp.forms import SignUpForm,SignInForm,ForgotPasswordForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(View):
    template_name = 'register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                # Check if the username or email is already taken
                if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                    messages.error(request, 'Username or email is already taken.')
                    return render(request, self.template_name, {'form': form})

                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                messages.success(request, 'Account created successfully. Please sign in.')
                return redirect('signin')  # Redirect to the sign-in page

            else:
                messages.error(request, 'Password and Confirm Password do not match.')
        return render(request, self.template_name, {'form': form})
    






class SignInView(View):
    template_name = 'login.html'

    def get(self, request):
        form = SignInForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully signed in.')
                return redirect('index')  # Redirect to the home page after sign-in
            else:
                messages.error(request, 'Invalid username or password.')

        return render(request, self.template_name, {'form': form})
    



class IndexView(TemplateView):
    template_name="index.html"


def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

