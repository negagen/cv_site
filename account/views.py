from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def user_info(request):
    return render(request, 'user_info.html')

def register(request):
    return render(request, 'register.html')