from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'App/home.html')

def event(request):
    return render(request,'App/event.html')

def members(request):
    return render(request,'App/members.html')