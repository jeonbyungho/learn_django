from django.shortcuts import render

def home(request):
   return render(request, 'singlepage/landing.html')

def about(request):
   return render(request, 'singlepage/about_me.html')