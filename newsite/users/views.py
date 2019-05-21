from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'User %s successfully created' % username)
            return redirect('user')
    else:
        form = UserOurRegistration()

    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация'})


# decorator like function login_required(profile(request))
@login_required
def profile(request):
    return render(request, 'users/profile.html')
