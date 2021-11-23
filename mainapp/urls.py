from django.urls import path
from .views import index, new, reports, detail

urlpatterns = [
    path('', index, name='home'),
    path('new/', new, name='new'),
    path('reports/', reports, name='reports'),
    path('detail/<int:id>/', detail, name='detail')
]