from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

def page2(request):
    return render(request, 'o_nas.html')