from django.shortcuts import render, redirect
from .models import Otchot, Otdel, Zagolovok, Description, Images
from .services import get_otchot, get_otchot_all, get_otdels, get_zagolovok, get_otdel_id, get_zag_id, get_images
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
        images = request.FILES.getlist('images')
        print('-------------', data)
        if data.get("otdel_title"):
            otchot = Otchot.objects.get(id=id)
            otdel, create = Otdel.objects.get_or_create(title=data['otdel_title'], otchot=otchot)
        if data.get("zag_title"):
            otdel = Otdel.objects.get(id=data.get("otdel_id"))
            zagolovok, create = Zagolovok.objects.get_or_create(title=data['zag_title'], otdel=otdel)
            if data.get("description"):
                description = Description.objects.get_or_create(text=data['description'], zagolovok=zagolovok)
        if images:
            for image in images:
                image = Images.objects.get_or_create(image=image, zagolovok=zagolovok)

    otdels = get_otdels(id)
    otchot_info = get_otchot(id)
    get_id = get_otdel_id(id)
    list_x = []
    zag_id = []
    image_list = []
    for i in get_id:
        x = i['id']
        list_x.extend(get_zagolovok(x))
        zag_id.extend(get_zag_id(x))
    for j in zag_id:
        image_list.extend(get_images(j['id']))
    print('/????????????', list_x)
    print('^^^^^^^^^^^^^^^^^^^^', image_list)
    ctx = {
        'otchot': otchot_info,
        'otdels': otdels,
        'list_x': list_x,
        'image_list': image_list
    }
    return render(request, 'detail.html', ctx)


def delete_zogolovok(request, otchot_id, zagolovok_id):
    Zagolovok.objects.get(id=zagolovok_id).delete()
    return redirect(f'http://127.0.0.1:8000/detail/{otchot_id}/')


def delete_otchot(request, otchot_id):
    Otchot.objects.get(id=otchot_id).delete()
    return redirect('http://127.0.0.1:8000/reports')


def delete_otdel(request, otchot_id, otdel_id):
    Otdel.objects.get(id=otdel_id).delete()
    return redirect(f'http://127.0.0.1:8000/detail/{otchot_id}/')


def otchot(request, otchot_id):
    otdels = get_otdels(otchot_id)
    otchot_info = get_otchot(otchot_id)
    get_id = get_otdel_id(otchot_id)
    list_x = []
    zag_id = []
    image_list = []
    for i in get_id:
        x = i['id']
        list_x.extend(get_zagolovok(x))
        zag_id.extend(get_zag_id(x))
    for j in zag_id:
        image_list.extend(get_images(j['id']))
    ctx = {
        'otchot': otchot_info,
        'otdels': otdels,
        'list_x': list_x,
        'image_list': image_list
    }
    return render(request, 'otchot.html', ctx)


def edit_otdel(request, otdel_id):
    otdel = Otdel.objects.get(id=otdel_id)
    if request.POST:
        data = request.POST
        if data.get('otdel_title'):
            otdel.title = data['otdel_title']
            otdel.save()
    ctx = {
        'otdel': otdel
    }
    return render(request, 'edit_otdel.html', ctx)


