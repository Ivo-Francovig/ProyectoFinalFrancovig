from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from django.db import models

#Modelos: Experiencia Profesional, Formacion Academica y Skills
  
class ExProf(models.Model):
    empresa = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)
    fechaInicial = models.CharField(max_length=40)
    fechaFinal = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=400)
    referencia = models.CharField(max_length=40)
    telefonoReferencia = models.IntegerField()

    def __str__(self) -> str:
        return f"Empresa: {self.empresa} - Puesto: {self.puesto} - Fecha de inicio: {self.fechaInicial} - Fecha de finalización: {self.fechaFinal} - Referencia: {self.referencia} - Telefono: {str(self.telefonoReferencia)}"

class Formacion(models.Model):
    institucion = models.CharField(max_length=40)
    nombreCurso = models.CharField(max_length=50)
    fechaInicial = models.CharField(max_length=40)
    fechaFinal = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    proyectoFinal = models.CharField(max_length=140)

    def __str__(self) -> str:
        return f"Institución: {self.institucion} - Nombre: {self.nombreCurso} - Fecha de inicio: {self.fechaInicial} - Fecha de finalización: {self.fechaFinal} - Estado: {self.estado}"    

class Skills(models.Model):
    software = models.CharField(max_length=40)
    nivel = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"Software: {self.software} - Nivel: {self.nivel}"   
