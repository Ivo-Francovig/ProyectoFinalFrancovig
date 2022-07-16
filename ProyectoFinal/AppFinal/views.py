from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppFinal.models import ExProf, Formacion, Skills
from AppFinal.forms import FormularioExProf, FormularioFormacion, FormularioSkills, UserRegisterForm
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Vistas

def inicio(self):
    plantilla = loader.get_template('AppFinal/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def experiencia(request):
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            experiencias = ExProf.objects.filter( Q(empresa_icontains=search) )
            return render(request, "AppFinal/experienciaprofesional.html", {"experiencias":experiencias, "search":True})
    experiencias = ExProf.objects.all()
    return render(request, "AppFinal/experienciaProfesional.html", {"experiencias":experiencias})

def formacion(request):
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            formaciones = Formacion.objects.filter( Q(institucion_icontains=search) )
            return render(request, "AppFinal/formacionacademica.html", {"formaciones":formaciones, "search":True})
    formaciones = Formacion.objects.all()
    return render(request, "AppFinal/formacionAcademica.html", {"formaciones":formaciones})

def skill(request):
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            skills = Skills.objects.filter( Q(software_icontains=search) )
            return render(request, "AppFinal/skills.html", {"skills":skills, "search":True})
    skills = Skills.objects.all()
    return render(request, "AppFinal/skills.html", {"skills":skills})

def perfil(self):
    plantilla = loader.get_template('AppFinal/perfil.html')
    documento = plantilla.render()
    return HttpResponse(documento)

#----------------------------------------------------------------
# FORMULARIOS:

def formularioExProf(request):
    if request.method == 'POST':
        miFormulario = FormularioExProf(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empresa = informacion['empresa']
            puesto = informacion['puesto']
            fechaInicial = informacion['fechaInicial']
            fechaFinal = informacion['fechaFinal']
            descripcion = informacion['descripcion']
            referencia = informacion['referencia']
            telefonoReferencia = informacion['telefonoReferencia']
            experiencia = ExProf(empresa=empresa, puesto=puesto, fechaInicial=fechaInicial, fechaFinal=fechaFinal, descripcion=descripcion, referencia=referencia, telefonoReferencia=telefonoReferencia)
            experiencia.save()
            return render(request, 'AppFinal/inicio.html')
    else:
        miFormulario = FormularioExProf()

    return render(request, 'AppFinal/formularioExProf.html', {"miFormulario":miFormulario})

def formularioFormacion(request):
    if request.method == 'POST':
        miFormulario = FormularioFormacion(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            institucion = informacion['institucion']
            nombreCurso = informacion['nombreCurso']
            fechaInicial = informacion['fechaInicial']
            fechaFinal = informacion['fechaFinal']
            estado = informacion['estado']
            proyectoFinal = informacion['proyectoFinal']
            formacion = Formacion(institucion=institucion, nombreCurso=nombreCurso, fechaInicial=fechaInicial, fechaFinal=fechaFinal, estado=estado, proyectoFinal=proyectoFinal)
            formacion.save()
            return render(request, 'AppFinal/inicio.html')
    else:
        miFormulario = FormularioFormacion()

    return render(request, 'AppFinal/formularioFormacion.html', {"miFormulario":miFormulario})

def formularioSkills(request):
    if request.method == 'POST':
        miFormulario = FormularioSkills(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            software = informacion['software']
            nivel = informacion['nivel']
            skill = Skills(software=software, nivel=nivel)
            skill.save()
            return render(request, 'AppFinal/inicio.html')
    else:
        miFormulario = FormularioSkills()

    return render(request, 'AppFinal/formularioSkills.html', {"miFormulario":miFormulario})

#----------------------------------------------------------------
# BUSQUEDA DE SKILLS POR NIVEL

def busquedaSkills(request):
    return render(request, 'AppFinal/busquedaSkills.html')

def busqueda(request):
    if request.GET['nivel']:
        nivel = request.GET['nivel']
        skills = Skills.objects.filter(nivel=nivel)
        return render(request, 'AppFinal/resultadosBusqueda.html', {'skills': skills, 'nivel': nivel})
    else:
        respuesta = "No dato ingresado no es válido, intente nuevamente."
    return HttpResponse(respuesta)

#----------------------------------------------------------------
# CRUD - CBV (Clases basadas en vistas)

# @login_required
class ExProfList(ListView):
    model = ExProf
    template_name = "AppFinal/experiencia_list.html"

class ExProfDetalle(DetailView):
    model = ExProf
    template_name = "AppFinal/exprof_detalle.html"

class ExProfCrear(CreateView):
    model = ExProf
    success_url = reverse_lazy("List")
    fields = ['empresa', 'puesto', 'fechaInicial', 'fechaFinal', 'descripcion', 'referencia', 'telefonoReferencia']

class ExProfUpdate(UpdateView):
    model = ExProf
    success_url = reverse_lazy("List")
    fields = ['empresa', 'puesto', 'fechaInicial', 'fechaFinal', 'descripcion', 'referencia', 'telefonoReferencia']

class ExProfDelete(DeleteView):
    model = ExProf
    success_url = reverse_lazy("List")


#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "AppFinal/inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "AppFinal/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppFinal/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "AppFinal/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "AppFinal/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "AppFinal/registro.html", {"form": form})