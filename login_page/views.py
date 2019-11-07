from django.shortcuts import render

def loginUser (request):

    return render(request, 'login_html.html')