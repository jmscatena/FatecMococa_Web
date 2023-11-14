from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=70, blank=False,null=False)
    descricao = models.CharField(max_length=250,)
    arquivo = models.FileField(upload_to='files/')
    capa = models.ImageField(upload_to='imagens/news/')
    data_publicacao = models.DateField(auto_now_add=True)