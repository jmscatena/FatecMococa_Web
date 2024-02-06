import os
from typing import Dict

from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from django.utils.text import slugify

from .models import *
import sweetify

def index(request,pk=None):
    noticias = []
    if request.path == '/noticias/':
        return render(request,'errors/404.html')
    if request.method == 'POST':
        create(request)
    elif request.method == 'GET' and pk is None:
        noticias = Noticia.objects.all()
        return render(request, 'noticias/edit.html',{'noticias':noticias})
    elif request.method == 'GET' and pk is not None:
        return render(request,'noticias/noticia.html',{'news':select(request,pk)})
    elif request.method == 'PATCH':
        update(request,pk)
    elif request.method == 'DELETE':
        destroy(request,pk)
    else:
        return render(request,'errors/404.html')

def edit(request):
    if request.method == "POST":
        create(request)
    return render(request,'noticias/add.html')
def create(request):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    #if tk != None:

    try:
        title = request.POST['titulo']
        description = request.POST['descricao']
        if 'capa' in request.FILES:
            cover = request.FILES['capa']
            basename, extension = os.path.splitext(os.path.basename(request.FILES['capa'].name))
            cover_nome = slugify(basename) + extension
            cover_up = SimpleUploadedFile(cover_nome, cover.read())
            cover_data: Dict[str, str]
        else:
            cover_up = './static/default_cover.png'
        if 'anexo' in request.FILES:
            attach = request.FILES['anexo']
            basename, extension = os.path.splitext(os.path.basename(request.FILES['anexo'].name))
            attach_nome = slugify(basename) + extension
            attach_up = SimpleUploadedFile(attach_nome, attach.read())
            attach_data: Dict[str, str]
        else:
            attach_up = './static/default.png'
        print(cover_up)
        new = Noticia(titulo=title,descricao=description, arquivo=attach_up,capa=cover_up)
        new.save()
        sweetify.success(request, 'Notícia Adicionada com Sucesso !', timer=5000)
    except Exception as ex:
            print(ex)
            sweetify.error(request, 'Erro ao Adicionar a Notícia !\nCódigo:'+str(ex), timer=10000)
            return ex
    #else: return 401  # Unauthorized
    #return render(request, 'noticias/add.html', {code: code, error: error})

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
    return render(request, 'noticias/edit.html', {'code': code, 'error': error})

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
    return render(request, 'noticias/edit.html', {'code': code, 'error': error})

def select(request,pk=None):
    #tk = request.session['tk'] if 'tk' in request.session else None
        error = None
    #if tk is not None:
        if pk is not None:
            try:
                news = Noticia.objects.get(id=int(pk))
                if news is not None:
                    code = 200  # OK
                    return news
                else:
                    code = 404 # Not Found
                    return None
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    #else: code = 401 # Unauthorized
        return render(request, 'noticias/edit.html', {'code': code, 'error': error})
def list(request):
    try:
        news = Noticia.objects.all()
        code = 200  # OK
        return render(request, 'noticias/edit.html', {'code': code, 'news':news})
    except Exception as ex:
            print(ex)
            code= 403 # Forbidden
            error = ex
    return render(request, 'noticias/edit.html', {'code': code, 'error': error})

    '''
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    news = None
    if tk is not None:
        try:
            news = Noticia.objects.all()
            code = 200  # OK
            return render(request, 'noticias/edit.html', {code: code, news:news})
        except Exception as ex:
                print(ex)
                code= 403 # Forbidden
                error = ex
    else: code = 401 # Unauthorized
    return render(request, 'noticias/edit.html', {code: code, error: error})
    '''

