from django.shortcuts import render

def index(request):
   return render(request, 'webapp/index.html', {'content': '안녕 파이썬'})