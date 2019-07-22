from django.db import models


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(verbose_name='کد دستگاه', db_index=True)
    operator_name = models.CharField(max_length=200, verbose_name='نام اپراتور')
    device_hour = models.FloatField(verbose_name='ساعت دستگاه')
    voltage_l1 = models.FloatField(verbose_name='ولتاژ L1')
    voltage_l2 = models.FloatField(verbose_name='ولتاژ L2')
    voltage_l3 = models.FloatField(verbose_name='ولتاژ L3')
    hertz = models.FloatField(verbose_name='Hz')
    amper_l1 = models.FloatField(verbose_name='آمپر L1')
    amper_l2 = models.FloatField(verbose_name='آمپر L2')
    amper_l3 = models.FloatField(verbose_name='آمپر L3')
    kw = models.FloatField(verbose_name='KW')
    oil_pressure = models.FloatField(verbose_name='فشار روغن')
    water_temperature = models.FloatField(verbose_name='دمای آب')
    battery_voltage = models.FloatField(verbose_name='ولتاژ باتری')
    power_meter_number = models.FloatField(verbose_name='شماره کنتور')
    gasoline_liters = models.FloatField(verbose_name='لیتراژ گازوئیل')
    description = models.TextField(verbose_name='توضیحات')
    datetime = models.DateTimeField(verbose_name='تاریخ و زمان')

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' , '.join(field_values)

    class Meta:
        verbose_name = 'دستگاه'
        verbose_name_plural = 'دستگاه ها'
