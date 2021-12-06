from django.contrib import admin
from .models import *
# Register your models here.


class OtchotAdmin(admin.ModelAdmin):
    exclude = ['slug']


class OtdelAdmin(admin.ModelAdmin):
    pass


class ZagolovokAdmin(admin.ModelAdmin):
    pass


class DefaultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Otchot, OtchotAdmin)
admin.site.register(Otdel, OtdelAdmin)
admin.site.register(Zagolovok, ZagolovokAdmin)
admin.site.register(Default, DefaultAdmin)
