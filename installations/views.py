from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from installations.forms import DeviceForm, EditDeviceForm
from django.utils.timezone import activate

from installations.tools import random_date, random_cumulative_num
from monitoring_system import settings
from autofixture import AutoFixture, generators
from installations.models import Device

activate(settings.TIME_ZONE)


def generate_fake_data():
    for i in range(100):
        fixture = AutoFixture(Device, field_values={'code': randint(1, 5),
                                                    'datetime': random_date(),
                                                    'operator_name': generators.StaticGenerator('admin'),
                                                    'gasoline_liters': randint(0, 2000),
                                                    'voltage_l1': randint(20, 400),
                                                    'voltage_l2': randint(20, 400),
                                                    'voltage_l3': randint(20, 400),
                                                    'amper_l1': randint(20, 4000),
                                                    'amper_l2': randint(20, 4000),
                                                    'amper_l3': randint(20, 4000),
                                                    'water_temperature': randint(-10, 3000),
                                                    'device_hour': random_cumulative_num(),
                                                    'hertz': randint(2000, 20000),
                                                    'kw': random_cumulative_num(),
                                                    })
        fixture.create(1)


@login_required()
def home(request):
    devices = Device.objects.order_by('code', '-datetime').distinct('code').all()
    return render(request, 'home.html', {'devices': devices})


@login_required()
def new_device(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.operator_name = request.user
            device.datetime = timezone.now()
            device.save()
            return HttpResponseRedirect('/')
    else:
        form = DeviceForm()
    return render(request, 'installations/new_device.html', {'form': form})


@login_required()
def edit_device(request, code):
    device = Device.objects.filter(code=code).first()
    if not device:
        raise Http404()
    if request.method == "POST":
        form = EditDeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.code = code
            device.operator_name = request.user
            device.datetime = timezone.now()
            device.save()
            return HttpResponseRedirect('/')
    else:
        form = EditDeviceForm()
    return render(request, 'installations/edit_device.html', {'form': form,
                                                              'device_code': device.code,
                                                              'user': request.user})


@login_required()
def detail_device(request, pk):
    device = Device.objects.filter(id=pk).first()
    return render(request, 'home.html', {'device': device})

# @login_required()
# def delete_device(request, code):
#     device = Device.objects.filter(code=code).all()
#     if not device:
#         raise Http404()
#     try:
#         device.delete()
#     except Exception as e:
#         raise e
#     return HttpResponseRedirect('/')
