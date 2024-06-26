# admin.py
from django.contrib import admin
from .models import Stylist, Client

class StylistAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','message','datetime')
    # other configurations if needed

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cphone','stylist','service','issent','appointmentdt')
    # other configurations if needed
    actions = ['send_sms_action']  # Add your custom action here

    def send_sms_action(self, request, queryset):
        # Implement your SMS sending logic here
        pass  # Replace with your logic

admin.site.register(Stylist, StylistAdmin)
admin.site.register(Client, ClientAdmin)
