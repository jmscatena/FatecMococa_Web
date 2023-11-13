from django.shortcuts import render
from .models import *
import sweetify
# Create your views here.

def index(request,pk=None):
    if request.method == 'POST':
        create(request)
    elif request.method == 'GET':
        return render(request, 'noticias/index.html')
    elif request.method == 'GET' and pk is not None:
        select(request, pk)
    elif request.method == 'PATCH':
        update(request,pk)
    elif request.method == 'DELETE':
        destroy(request,pk)
    else:
        return render(request,'errors/404.html')

def edit(request):
    if request.method == "POST":
        create(request)
    else: return render(request,'noticias/edit.html',{'code':200})
def create(request):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk != None:
        try:
            title = request.POST['titulo']
            description = request.POST['descricao']
            file = request.FILES['arquivo'] if 'arquivo' in request.POST else './static/default.png'
            cover = request.FILES['capa'] if 'capa' in request.POST else './static/default_cover.png'
            new = Noticia(titulo=title,descricao=description, arquivo=file,capa=cover)
            new.save()
            code=201
            sweetify.toast(request, 'Adicionado com Sucesso!!!', icon="success", timer=3000)
        except Exception as ex:
                print(ex)
                sweetify.toast(request, 'Error ao Adicionar!', icon="error", timer=3000)
                code = ex
    else: code = 401  # Unauthorized
    return render(request, 'noticias/edit.html', {code: code, error: error})

def destroy(request,pk=None):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk is not None:
        if pk is not None:
            try:
                new = Noticia.object.get(id=pk)
                if new is not None:
                    new.delete()
                    code = 202 # Accept
                else:
                    code = 404 # Not Found
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    else: code = 401 # Unauthorized
    return render(request, 'noticias/index.html', {code: code, error: error})

def update(request, pk=None):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk is not None:
        if pk is not None:
            try:
                new = Noticia.object.get(id=pk)
                if new is not None:
                    new.titulo = request.POST['titulo']
                    new.descricao = request.POST['descricao']
                    new.arquivo = request.POST['descricao'] if 'descricao' in request.FILES else new.arquivo
                    new.capa = request.POST['capa'] if 'capa' in request.FILES else new.capa
                    new.save()
                    code = 200 # OK
                else:
                    code = 404 # Not Found
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    else: code = 401 # Unauthorized
    return render(request, 'noticias/index.html', {code: code, error: error})

def select(request,pk=None):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk is not None:
        if pk is not None:
            try:
                new = Noticia.object.get(id=pk)
                if new is not None:
                    code = 200  # OK
                    return render(request, 'noticias/index.html', {code: code, new:new})
                else:
                    code = 404 # Not Found
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    else: code = 401 # Unauthorized
    return render(request, 'noticias/index.html', {code: code, error: error})
def list(request):
    try:
        news = Noticia.objects.all()
        code = 200  # OK
        return render(request, 'noticias/index.html', {code: code, news:news})
    except Exception as ex:
            print(ex)
            code= 403 # Forbidden
            error = ex
    return render(request, 'noticias/index.html', {code: code, error: error})

    '''
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    news = None
    if tk is not None:
        try:
            news = Noticia.objects.all()
            code = 200  # OK
            return render(request, 'noticias/index.html', {code: code, news:news})
        except Exception as ex:
                print(ex)
                code= 403 # Forbidden
                error = ex
    else: code = 401 # Unauthorized
    return render(request, 'noticias/index.html', {code: code, error: error})
    '''
