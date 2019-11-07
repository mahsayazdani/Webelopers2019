from django.shortcuts import render
from django.contrib.auth import authenticate, login


def loginUser(request):
    print('dtfguyh')
    if request.POST:
        invalid = False
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.

        else:
            # Return an 'invalid login' error message.
            print("hi")
            invalid = True

        return render(request, 'logged_in.html', {'invalid': invalid})
    return render(request, 'login_html.html')



