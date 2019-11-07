from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from register_page import forms
from register_page.forms import SignUpForm


def registerUser (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # if User.objects.filter(username=form.cleaned_data['username']).exists():
            #     raise forms.ValidationError(u'Username "%s" is already in use.' )
            # else:
            username = form.cleaned_data.get('username')


            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register_html.html', {'form': form})


