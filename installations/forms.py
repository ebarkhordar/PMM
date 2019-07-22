from django import forms

from .models import Device
from django.utils.translation import ugettext_lazy as _


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['operator_name', 'datetime']


voltage_range = range(0, 300)
amper_range = range(0, 1200)

not_in_range_error = 'عدد وارد شده در محدوده معتبر نیست!'


class EditDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['operator_name', 'datetime', 'code']

    def clean_voltage_l1(self):
        if int(self.cleaned_data['voltage_l1']) in voltage_range:
            return self.cleaned_data['voltage_l1']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_voltage_l2(self):
        if int(self.cleaned_data['voltage_l2']) in voltage_range:
            return self.cleaned_data['voltage_l2']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_voltage_l3(self):
        if int(self.cleaned_data['voltage_l3']) in voltage_range:
            return self.cleaned_data['voltage_l3']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_amper_l1(self):
        if int(self.cleaned_data['amper_l1']) in amper_range:
            return self.cleaned_data['amper_l1']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_amper_l2(self):
        if int(self.cleaned_data['amper_l2']) in amper_range:
            return self.cleaned_data['amper_l2']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_amper_l3(self):
        if int(self.cleaned_data['amper_l3']) in amper_range:
            return self.cleaned_data['amper_l3']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_water_temperature(self):
        if int(self.cleaned_data['water_temperature']) in range(0, 200):
            return self.cleaned_data['water_temperature']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_gasoline_liters(self):
        if int(self.cleaned_data['gasoline_liters']) in range(0, 20000):
            return self.cleaned_data['gasoline_liters']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_oil_pressure(self):
        if int(self.cleaned_data['oil_pressure']) in range(0, 20):
            return self.cleaned_data['oil_pressure']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_kw(self):
        if int(self.cleaned_data['kw']) in range(0, 1000):
            return self.cleaned_data['kw']
        else:
            raise forms.ValidationError(_(not_in_range_error))

    def clean_battery_voltage(self):
        if int(self.cleaned_data['battery_voltage']) in range(0, 50):
            return self.cleaned_data['battery_voltage']
        else:
            raise forms.ValidationError(_(not_in_range_error))
