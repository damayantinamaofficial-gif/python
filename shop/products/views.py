from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'shop_name': 'My Shop'
    }
    #return HttpResponse("Home page")
    return render(request,'home.html',context)