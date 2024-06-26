# models.py
from django.db import models

class Stylist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Stylist Name')
    phone = models.CharField(max_length=20, verbose_name='Stylist Phone Number')
    message = models.TextField(verbose_name='Message')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Date / Time')

    def __str__(self):
        return self.name


class Client(models.Model):
    cname = models.CharField(max_length=100, verbose_name='Client Name')
    cphone = models.CharField(max_length=11, verbose_name='Client Phone Number')
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, verbose_name='Stylist Name')
    service = models.CharField(max_length=200, verbose_name='Service')
    issent = models.BooleanField(default=False, verbose_name='Has a message been Sent?')
    appointmentdt = models.DateTimeField(verbose_name='Time and Date of appointment')

    def __str__(self):
        return self.cname

