from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def loginUser(request):
    if request.POST:
        invalid = False
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home_html.html')

        else:
            # Return an 'invalid login' error message.
            invalid = True
            return render(request, 'login_html.html', {'invalid': invalid})


    return render(request, 'login_html.html')



