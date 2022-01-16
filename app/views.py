from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from app.forms import DepartmentForm, UnitForm
from app.models import BigDepartment, Unit, Vocabulary
from user.models import CustomUser


def home(request):
    return render(request, 'app/home.html')


def department_(request):
    user = CustomUser.objects.get(username=request.user.username)
    return render(request, 'user/base.html', {'user': user})


def add_deparment(request):
    user = CustomUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            unit = BigDepartment()
            unit.name = form.cleaned_data['name']
            unit.description = form.cleaned_data['description']
            if request.FILES:
                unit.image = request.FILES['image']
            else:
                unit.image = form.cleaned_data['image']
            unit.user = user
            unit.save()
            messages.success(request, 'Your a new department has added successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Department does not add!')
            return redirect('add-department')
    form = DepartmentForm()
    return render(request, 'app/add_department.html', {'form': form})


def department_detail(request, uuid):
    user = CustomUser.objects.get(username=request.user.username)
    department = BigDepartment.objects.get(user=user, id=uuid)
    units = Unit.objects.filter(department=department)
    return render(request, 'app/department_detail.html', {'department': department, 'units': units})


def add_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            unit = Unit()
            unit.title = form.cleaned_data['title']
            unit.description = form.cleaned_data['description']
            if request.FILES:
                unit.image = request.FILES['image']
            else:
                unit.image = form.cleaned_data['image']
            unit.department = form.cleaned_data['department']
            unit.save()
            messages.success(request, 'Your a new department has added successfully')
            return redirect('home')
        else:
            messages.warning(request, 'Department does not add!')
            return redirect('add-unit')
    form = UnitForm()
    return render(request, 'app/add_unit.html', {'form': form})


def unit_vocabulary(request, uuid):
    unit = Unit.objects.get(id=uuid)
    vocabulary = Vocabulary.objects.filter(unit=unit)
    return render(request, 'app/unit_vocabulary.html', {'vocabulary': vocabulary})
