from django.urls import path
from .views import index, new, reports, detail, delete_zogolovok, delete_otchot, delete_otdel, otchot,\
    edit_otdel, edit_zagolovok, html_pdf

urlpatterns = [
    path('', index, name='home'),
    path('new/', new, name='new'),
    path('reports/', reports, name='reports'),
    path('detail/<int:id>/', detail, name='detail'),
    path('delete/otchot/<int:otchot_id>', delete_otchot, name='delete-otchot'),
    path('delete/otdel/<int:otchot_id>/<int:otdel_id>', delete_otdel, name='delete-otdel'),
    path('delete/zagolovok/<int:otchot_id>/<int:zagolovok_id>', delete_zogolovok, name='delete-zagolovok'),
    path('otchot/<int:otchot_id>', otchot, name='otchot'),
    path('edit/otdel/<int:otdel_id>', edit_otdel, name='edit-otdel'),
    path('edit/zagolovok/<int:otdel_id>/<int:zagolovok_id>', edit_zagolovok, name='edit-zagolovok'),
    path('pdf/<int:otchot_id>', html_pdf, name='pdf')
]