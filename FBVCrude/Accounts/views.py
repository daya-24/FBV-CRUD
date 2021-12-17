from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginview(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('pw')
        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request, user)
            return redirect('show_lap')
        else:
            messages.error(request, 'Invalid Crednitial!')

    context = {}
    templates_name = 'Accounts/login.html'
    return render(request, templates_name, context)

def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login1')

    context = {'form': form}
    templates_name = 'Accounts/register.html'
    return render(request, templates_name, context)

def logoutView(request):
    logout(request)
    return redirect('login1')