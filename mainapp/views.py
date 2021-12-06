from django.shortcuts import render, redirect, HttpResponse
from .models import Otchot, Otdel, Zagolovok, Description, Images, Default
from .services import get_otchot, get_otchot_all, get_otdels, get_zagolovok,\
    get_otdel_id, get_zag_id, get_images, get_descriptions
from django.template.loader import get_template
# noinspection PyUnresolvedReferences
import pdfkit
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def new(request):
    if request.POST:
        data = request.POST
        if data.get('otchot_name'):
            otchot, create = Otchot.objects.get_or_create(
                name=data['otchot_name'],
                company=data['company'],
                client=data['client'],
                order=data['order'])
        return redirect(f'/detail/{otchot.id}/')
    default = Default.objects.get()
    ctx = {'default': default}
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
    description_list = []
    for i in get_id:
        x = i['id']
        list_x.extend(get_zagolovok(x))
        zag_id.extend(get_zag_id(x))
    for j in zag_id:
        image_list.extend(get_images(j['id']))
        description_list.extend(get_descriptions(j['id']))
    ctx = {
        'otchot': otchot_info,
        'otdels': otdels,
        'list_x': list_x,
        'image_list': image_list,
        'description_list': description_list
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


def delete_image(request, otdel_id, zagolovok_id, image_id):
    Images.objects.get(id=image_id).delete()
    return redirect(f"http://127.0.0.1:8000/edit/zagolovok/{otdel_id}/{zagolovok_id}")


def otchot(request, otchot_id):
    otdels = get_otdels(otchot_id)
    otchot_info = get_otchot(otchot_id)
    get_id = get_otdel_id(otchot_id)
    list_x = []
    zag_id = []
    image_list = []
    description_list = []
    for i in get_id:
        x = i['id']
        list_x.extend(get_zagolovok(x))
        zag_id.extend(get_zag_id(x))
    for j in zag_id:
        image_list.extend(get_images(j['id']))
        description_list.extend(get_descriptions(j['id']))
    ctx = {
        'otchot': otchot_info,
        'otdels': otdels,
        'list_x': list_x,
        'image_list': image_list,
        'description_list': description_list
    }
    return render(request, 'otchot.html', ctx)


def edit_otdel(request, otdel_id):
    otdel = Otdel.objects.get(id=otdel_id)
    if request.POST:
        data = request.POST
        if data.get('otdel_title'):
            otdel.title = data['otdel_title']
            otdel.save()
        return redirect(f"http://127.0.0.1:8000/detail/{otdel.otchot_id}/")
    ctx = {
        'otdel': otdel
    }
    return render(request, 'edit_otdel.html', ctx)


def edit_zagolovok(request, zagolovok_id, otdel_id):
    otdel = Otdel.objects.get(id=otdel_id)
    zagolovok = Zagolovok.objects.get(id=zagolovok_id)
    if request.POST:
        data = request.POST
        print('^^^^^^^^^^^', data)
        if data.get('zagolovok_title'):
            zagolovok.title = data['zagolovok_title']
            zagolovok.save()
            if data.get('new_description'):
                description = Description.objects.get(zagolovok_id=zagolovok_id)
                description.text = data['new_description']
                description.save()
            return redirect(f"http://127.0.0.1:8000/detail/{otdel.otchot_id}/")
        if data.get('images'):
            images = request.POST.getlist('images')
            print('###########', images)
            for image in images:
                create = Images.objects.create(image=f'static/img/{image}', zagolovok=zagolovok)
            return redirect(f"http://127.0.0.1:8000/edit/zagolovok/{otdel_id}/{zagolovok_id}")
    images = get_images(zagolovok_id)
    description_list = get_descriptions(zagolovok_id)
    ctx = {
        'otdel': otdel,
        'description_list': description_list,
        'zagolovok': zagolovok,
        'images': images
    }
    return render(request, 'edit_zagolovok.html', ctx)


def html_pdf(request, otchot_id):
    otdels = get_otdels(otchot_id)
    otchot_info = get_otchot(otchot_id)
    get_id = get_otdel_id(otchot_id)
    list_x = []
    zag_id = []
    image_list = []
    description_list = []
    for i in get_id:
        x = i['id']
        list_x.extend(get_zagolovok(x))
        zag_id.extend(get_zag_id(x))
    for j in zag_id:
        image_list.extend(get_images(j['id']))
        description_list.extend(get_descriptions(j['id']))
    ctx = {
        'otchot': otchot_info,
        'otdels': otdels,
        'list_x': list_x,
        'image_list': image_list,
        'description_list': description_list
    }
    template = get_template('otchot_to_PDF.html')
    html = template.render(ctx)
    pdf = pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Otchot.pdf" '
    response.write(pdf)
    return response