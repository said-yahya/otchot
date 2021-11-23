from django.shortcuts import render, redirect
from .models import Otchot, Otdel, Zagolovok, Description, Images
from .services import get_otchot, get_otchot_all, get_otdels, get_zagolovok
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def new(request):
    if request.POST:
        data = request.POST
        if data['otchot_name'] != '':
            otchot, create = Otchot.objects.get_or_create(name=data['otchot_name'])
        return redirect(f'/detail/{otchot.id}/')
    ctx = {}
    return render(request, 'add.html', ctx)


def reports(request):
    otchoti = get_otchot_all()
    ctx = {
        'otchoti': otchoti
    }
    return render(request, 'report.html', ctx)


def detail(request, id):
    if request.POST:
        data = request.POST
        print('-------------', data)
        if data['otdel_title']:
            otchot = Otchot.objects.get(id=id)
            otdel, create = Otdel.objects.get_or_create(title=data['otdel_title'], otchot=otchot)
        if data['zag_title']:
            zagolovok, create = Zagolovok.objects.get_or_create(title=data['zag_title'], otdel=otdel)
            if data['description']:
                description = Description.objects.get_or_create(text=data['description'], zagolovok=zagolovok)

    otdels = get_otdels(id)
    otchot_info = get_otchot(id)
    ctx = {
        'otchot': otchot_info,
        'otdels': otdels,
    }
    return render(request, 'detail.html', ctx)


# def add_zagolovok(request, id):
#     if request.POST:
#         data = request.POST
#         print('#######', data)
#         images = request.FILES.getlist('images')
#         if data['title'] != '':
#             zagolovok, created = Zagolovok.objects.get_or_create(
#                 title=data['title'],
#                 otdel_id=id)
#
#         if images:
#             for image in images:
#                 image = Images.objects.create(
#                     image=image,
#                     zagolovok=zagolovok)
#
#         if data['description'] != '':
#             description = Description.objects.create(
#                 text=data['description'],
#                 zagolovok=zagolovok)
#     zag = get_zagolovok(id)
#     for i in zag:
#         print('>>>>>>>>>>>>>>>>', i)
#     ctx = {
#
#     }
#     return render(request, 'zagolovok.html', ctx)