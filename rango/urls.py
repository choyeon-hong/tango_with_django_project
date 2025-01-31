from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'), #1st parameter : url path
]