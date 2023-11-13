from django.shortcuts import render

from news.models import Noticia


def home(request):
    noticias = Noticia.objects.all() if Noticia.objects.all() is not None else None
    return render(request,'base/index.html',{'noticias':noticias})


def cursos(request,nome):
    cursos = {'agro','ads','ads_ams','gti','ge','ge_ead','grh'}
    page = 'cursos/'+nome+'.html' if nome in cursos else 'errors/404.html'
    return render(request,page)


def institucional(request, nome):
    paginas = {'secretaria','calendario','cpa','cepe','cipa','congregacao','contas','convenios','diretoria','ds','quemsomos','ti'}
    page = 'institucional/'+nome+'.html' if nome in paginas else 'errors/404.html'
    return render(request,page)


def alunos(request, nome):
    paginas = {'estagios','horario_aulas','monitoria','tg'}
    page = 'alunos/'+nome+'.html' if nome in paginas else 'errors/404.html'
    return render(request,page)


def professores(request, nome):
    paginas = {'corpodocente','auxdoc'}
    page = 'professores/'+nome+'.html' if nome in paginas else 'errors/404.html'
    return render(request,page)
