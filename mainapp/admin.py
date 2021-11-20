from django.contrib import admin
from .models import *
# Register your models here.


class OtchotAdmin(admin.ModelAdmin):
    exclude = ['slug']


class OtdelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Otchot, OtchotAdmin)
admin.site.register(Otdel, OtdelAdmin)