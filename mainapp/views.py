from django.shortcuts import render
from .forms import OtchotForm, OtdelForm, ZagolovokForm
from .models import Otchot
from .services import get_otchot, get_otchot_all, get_otdels
# Create your views here.


def index(request):
    if request.POST:
        form = OtchotForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {})


def new(request):
    new_otchot = OtchotForm()
    ctx = {
        'new_otchot': new_otchot
    }
    return render(request, 'add.html', ctx)


def reports(request):
    form = OtchotForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
    otchoti = get_otchot_all()
    ctx = {
        'otchoti': otchoti
    }
    return render(request, 'report.html', ctx)


def detail(request, id):
    if request.POST:
        form = OtdelForm(request.POST)
        otchot = Otchot.objects.get(id=id)
        if form.is_valid():
            form.save(otchot)
    otdel_form = OtdelForm()
    zagolovok_form = ZagolovokForm()
    otdels = get_otdels(id)
    otchot_info = get_otchot(id)
    ctx = {
        'otchot': otchot_info,
        'otdel_form': otdel_form,
        'otdels': otdels,
        'zagolovok_form': zagolovok_form
    }
    return render(request, 'detail.html', ctx)


def add_zagolovok(request):
    ctx = {

    }
    return render(request, 'detail.html', ctx)