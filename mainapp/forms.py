from django import forms
from .models import Otchot, Otdel, Zagolovok


class OtchotForm(forms.ModelForm):
    class Meta:
        model = Otchot
        fields = ['name']


class OtdelForm(forms.ModelForm):
    title = forms.CharField(label='Название отдела', max_length=100)


class ZagolovokForm(forms.ModelForm):
    class Meta:
        model = Zagolovok
        fields = ['title']

    def save(self, otdel, commit=True):
        self.instance.otdel = otdel
        super().save()
        return self.instance

