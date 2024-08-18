from django.db import models
from datetime import date
# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=70, blank=False,null=False)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='files/')
    capa = models.ImageField(upload_to='imagens/news/')
    data_publicacao = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now_add=False, default=date.today())

    class Meta:
        ordering = ['-data_publicacao']