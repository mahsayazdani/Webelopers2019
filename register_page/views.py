from django.shortcuts import render

def registerUser (request):

    return render(request, 'register_html.html')
