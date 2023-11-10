from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # If user is submitting the form, authenticate the user
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )

        if user is not None:
            # If user is authenticated, log the user in
            login(request, user)
            return redirect('user_info')
        else:
            # If user is not authenticated, return error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_info(request):
    if not request.user.is_authenticated:
        # If user is not logged in, redirect to login page
        return redirect('login')
    return render(request, 'user_info.html', {'user': request.user})

def register(request):
    
    if request.method == 'POST':
        try:
            password1=request.POST['password1']
            password2=request.POST['password2']

            if password1 != password2:
                return render(request, 'register.html', {'error': 'Passwords do not match'})

            # If user is submitting the form, create a new user
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
            )
        except Exception as e:
            return render(request, 'register.html', {'error': e})
        return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    # Log out the user and redirect to login page
    logout(request)
    return redirect('login')