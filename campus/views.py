from django.shortcuts import render
from mailing.views import *

# Create your views here.

def campus_page(request):
   
    return render(request, 'campus/index.html')
