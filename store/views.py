from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, "store/index.html")


def login(request):
    return render(request, "store/auth/login.html" )

def register(request):
    return render(request, "store/auth/register.html" )