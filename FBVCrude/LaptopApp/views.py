from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login1')
def AddLaptopView(request):
    form = LaptopModelForm
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_lap')
        else:
            print('Form is INVALID')


    context = {'form':form}
    templates_name = 'LaptopApp/add_lap.html'
    return render(request, templates_name, context)


def ShowLaptopView(request):
    show_obj = Laptop.objects.all()
    context = {'show_obj': show_obj}
    templates_name = 'LaptopApp/show_lap.html'
    return render(request, templates_name, context)


@login_required(login_url='login1')
def UpdateLaptopView(request,i):
    update_obj = Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=update_obj)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST, instance=update_obj)
        if form.is_valid():
            form.save()
            return redirect('show_lap')


    context = {'form':form}
    templates_name = 'LaptopAPP/add_lap.html'
    return render(request, templates_name, context)


@login_required(login_url='login1')
def DeleteLaptopView(request, i):
    lap = Laptop.objects.get(id=i)
    lap.delete()
    return redirect('show_lap')
