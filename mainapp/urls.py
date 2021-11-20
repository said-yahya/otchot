from django.urls import path
from .views import index, new, reports, detail, add_zagolovok


urlpatterns = [
    path('', index, name='home'),
    path('new/', new, name='new'),
    path('reports/', reports, name='reports'),
    path('detail/<int:id>/', detail, name='detail'),
    path('add/zagolovok/<int:id>', add_zagolovok, name='zagolovok')
]