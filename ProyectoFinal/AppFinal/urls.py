from django.urls import path
from AppFinal.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name='inicio'),
    path('experiencia', experiencia , name='experiencia'),
    path('formacion', formacion, name='formacion'),
    path('habilidades', skill, name='habilidades'),
    path('formularioExProf', formularioExProf, name='formularioExProf'),
    path('formularioFormacion', formularioFormacion, name='formularioFormacion'),
    path('formularioSkills', formularioSkills, name='formularioSkills'),
    path('busquedaSkills', busquedaSkills,name='busquedaSkills'),
    path('busqueda', busqueda, name='busqueda'),
    path('perfil', perfil, name='perfil'),

    path('experiencia/list', ExProfList.as_view(), name='List'),
    path(r'^/(?P<pk>\d+)$', ExProfDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', ExProfCrear.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', ExProfUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', ExProfDelete.as_view(), name='Delete'),

    path('login', login_request, name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppFinal/logout.html'), name='logout'),
]
    