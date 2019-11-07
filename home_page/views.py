from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def startMainPage(request):
    # return HttpResponse("welcome")

    return render(request, 'home_html.html')
