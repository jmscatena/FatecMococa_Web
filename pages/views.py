from django.shortcuts import render
from models import *
def index(request,pk=None):
    if request.method == 'POST':
        create(request)
    elif request.method == 'GET':
        list(request)
    elif request.method == 'GET' and pk is not None:
        select(request, pk)
    elif request.method == 'PATCH':
        update(request,pk)
    elif request.method == 'DELETE':
        destroy(request,pk)
    else:
        return render(request,'errors/404.html')

def create(request):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    grupo = None
    if tk != None:
        try:
            if request.POST['gid'] == 0:
                gtit = request.POST['gtitulo']
                gdesc = request.POST['gdesc']
                grupo = Grupo(titulo=gtit,descricao=gdesc)
                grupo.save()
            elif 'gid' in request.POST:
                grupo = Grupo.object.get(id=int(request.POST['gid']))
            title = request.POST['titulo']
            text = request.POST['texto']
            header = request.POST['cabecalho']
            file = request.FILES['arquivo'] if 'arquivo' in request.POST else './static/page_default.png'
            cover = request.FILES['capa'] if 'capa' in request.POST else './static/page_cover_default.png'
            page = Pagina(titulo=title,texto=text, cabecalho=header,arquivo=file,capa=cover)
            if grupo is not None:
                page.grupo = grupo
            page.save()
            code = 201
        except Exception as ex:
                print(ex)
                code = ex
    else: code = 401  # Unauthorized
    return render(request, 'paginas/index.html', {code: code, error: error})

def destroy(request,pk=None):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk is not None:
        if pk is not None:
            try:
                page = Pagina.object.get(id=pk)
                if page is not None:
                    page.delete()
                    code = 202 # Accept
                else:
                    code = 404 # Not Found
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    else: code = 401 # Unauthorized
    return render(request, 'paginas/index.html', {code: code, error: error})

def update(request, pk=None):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk is not None:
        if pk is not None:
            try:
                page = Pagina.object.get(id=pk)
                grupo = Grupo.object.get(id=int(request.POST['gid'])) if 'gid' in request.POST else None
                if page is not None:
                    title = request.POST['titulo']
                    text = request.POST['texto']
                    header = request.POST['cabecalho']
                    file = request.FILES['arquivo'] if 'arquivo' in request.POST else './static/page_default.png'
                    cover = request.FILES['capa'] if 'capa' in request.POST else './static/page_cover_default.png'
                    page = Pagina(titulo=title, texto=text, cabecalho=header, arquivo=file, capa=cover)
                    if grupo is not None:
                        page.grupo = grupo
                    page.save()
                    code = 200 # OK
                else:
                    code = 404 # Not Found
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    else: code = 401 # Unauthorized
    return render(request, 'paginas/index.html', {code: code, error: error})

def select(request,pk=None):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    if tk is not None:
        if pk is not None:
            try:
                page = Pagina.object.get(id=pk)
                if page is not None:
                    code = 200  # OK
                    return render(request, 'paginas/index.html', {code: code, page:page})
                else:
                    code = 404 # Not Found
            except Exception as ex:
                    print(ex)
                    code= 403 # Forbidden
                    error = ex
        else: code = 405 # Not Allowed
    else: code = 401 # Unauthorized
    return render(request, 'paginas/index.html', {code: code, error: error})
def list(request):
    tk = request.session['tk'] if 'tk' in request.session else None
    error = None
    news = None
    if tk is not None:
        try:
            pages = Pagina.objects.all()
            if pages is not None:
                code = 200  # OK
                return render(request, 'paginas/index.html', {code: code, pages:pages})
            else:
                code = 404 # Not Found
        except Exception as ex:
                print(ex)
                code= 403 # Forbidden
                error = ex
    else: code = 401 # Unauthorized
    return render(request, 'paginas/index.html', {code: code, error: error})

