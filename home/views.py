from django.shortcuts import render

def home(request):
    """
    主页
    """
    return render(request, 'home/home.html')


# Create your views here.
