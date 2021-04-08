from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'App/home.html')

def events(request):
    return render(request,'App/events.html')

def members(request):
    return render(request,'App/members.html')