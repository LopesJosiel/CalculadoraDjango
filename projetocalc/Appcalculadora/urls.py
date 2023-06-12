from django.urls import path
from . import views
urlpatterns = [
    path ('', views.myfunctioncall, name='index'),
    path ('about', views.myfunctionabout, name='index'),
    path ('calcpage', views.calcpage, name = 'calcpage')
]
