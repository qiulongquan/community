from django.shortcuts import render,redirect

def home(request):
    """
    主页
    """
    return render(request, 'home/home.html')
    # return redirect('questions:question_list')
# Create your views here.