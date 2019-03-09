from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def error(request):
    return render(request, 'mainapp/error.html')