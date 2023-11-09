from django.shortcuts import render

def Home(request):
    return render(request,"screens/index.html")