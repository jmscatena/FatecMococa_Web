from django.shortcuts import render

def home(request):
    return render(request,'base/index.html')


def cursos(request,nome):
    cursos = {'agro','ads','gti','ge','ge_ead','grh'}
    page = 'cursos/'+nome+'.html' if nome in cursos else 'errors/404.html'
    return render(request,page)


def institucional(request, nome):
    paginas = {'secretaria','calendario','cepe','cipa','congregacao','contas','convenios','diretoria','ds','quemsomos','ti'}
    page = 'institucional/'+nome+'.html' if nome in paginas else 'errors/404.html'
    return render(request,page)


def alunos(request, nome):
    paginas = {'estagios','horario_aulas','monitoria','tg'}
    page = 'alunos/'+nome+'.html' if nome in paginas else 'errors/404.html'
    return render(request,page)
