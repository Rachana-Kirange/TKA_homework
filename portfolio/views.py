from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'portfolio/home.html')

def resumeview(request):
    return render(request, "portfolio/resume.html")