# views.py
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .utils import send_email_to_
import uuid
from .models import EmailVerification
from django.contrib import messages
from django.views import View


def home(request):
    classes = 'font-bold text-blue-600 hover:text-red-900 w-60 text-center border border-1 border-black p-2 rounded-2xl hover:bg-violet-900 hover:text-white mx-auto'
    return render(request, 'home.html', {'classes': classes})


class Signup(View):
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False 
            user.save()

            token = uuid.uuid4()
            EmailVerificationObject = EmailVerification(user=user, token=token)
            EmailVerificationObject.save()

            try:
                send_email_to_(request, user.email, token)
                messages.success(request, "Your account has been created successfully, please check your email to verify your account.")
                return redirect('signin')
            except Exception as e:
                messages.error(request, "There was an error sending the verification email. Please try again later.")
                user.delete() 
                return render(request, 'signup.html', {'form': form})
        else:
            messages.error(request, "Please correct the errors below.")
        return render(request, 'signup.html', {'form': form})




def email_verify(request, token):
    try:
        EmailVerificationObject = EmailVerification.objects.get(token=token)
        
        EmailVerificationObject.user.is_active = True
        EmailVerificationObject.user.save()
        
        EmailVerificationObject.delete()
        
        messages.success(request, "Email verified successfully. You can now log in.")
        return redirect('signin')  
    except EmailVerification.DoesNotExist:
        messages.error(request, "Invalid or expired verification token.")
        return redirect('home')



class Singin(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'signin.html', context)
    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {
            'form':form
        }
        return render(request, 'signin.html', context)

def logout_view(request):
    logout(request)
    return redirect('signin')