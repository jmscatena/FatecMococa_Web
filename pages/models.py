from django.db import models

# Create your models here.
class Grupo(models.Model):
    titulo = models.CharField(max_length=30, blank=False,null=False)
    descricao = models.CharField(max_length=250, blank=False,null=False)

class Pagina(models.Model):
    titulo = models.CharField(max_length=30, blank=False,null=False)
    texto = models.CharField(max_length=250, blank=False,null=False)
    logo = models.ImageField(upload_to='pages/logos/')
    cabecalho = models.ImageField(upload_to='pages/headers/')
    arquivo = models.FileField(upload_to='pages/files/')
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)

