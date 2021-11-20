from django import forms
from .models import Otchot, Otdel, Zagolovok


class OtchotForm(forms.ModelForm):
    class Meta:
        model = Otchot
        fields = ['name']


class OtdelForm(forms.ModelForm):
    class Meta:
        model = Otdel
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, otchot, commit=True):
        self.instance.otchot = otchot
        super().save()
        return self.instance


class ZagolovokForm(forms.ModelForm):
    class Meta:
        model = Zagolovok
        fields = ['title']

    def save(self, otdel, commit=True):
        self.instance.otdel = otdel
        super().save()
        return self.instance

