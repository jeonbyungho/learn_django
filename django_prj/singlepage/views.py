from django.shortcuts import render

def home(request):
   return render(request, 'singlepage/landing.html')