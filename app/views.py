from django.shortcuts import render

# Create your views here.

def staticos(request):
    return render(request,'staticos.html')