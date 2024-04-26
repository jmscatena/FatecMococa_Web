from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from news.models import Noticia

def login(request):
    if request.method == 'GET':
        return render(request, 'login/index.html')
    elif request.method == 'POST':
        u = User.objects.get(username=request.POST["user"])
        dados = {'user','pwd'}
        if ('user' in request.POST) and ('pwd' in request.POST):
            username = authenticate(username=request.POST['user'], password=request.POST['pwd'])
            if username is not None:
                user = User.objects.get(username=username)
                print(user.is_superuser)
                request.session.set_expiry(180)
                request.session['nome'] = user.first_name
                return render(request,'noticias/edit.html')
            return render(request,'login/login.html',context={'error':'Acesso Negado!'})
        else:
            return render(request,'login/login.html',context={'error':'Acesso Negado!'})
    else: return render(request,'errors/404.html')

def logout(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return home(request)


def home(request):
    noticias = Noticia.objects.all() if Noticia.objects.all() is not None else None
    return render(request,'base/index.html',{'noticias':noticias})

def cursos(request,nome):
    cursos = {'agro','ads','ads_ams','gti','ge','ge_ead','grh'}
    page = 'cursos/'+nome+'.html' if nome in cursos else 'errors/404.html'
    return render(request,page)

def grades(request,nome):
    cursos = {'agro','ads','ads_ams','gti','ge','ge_ead','grh'}
    page = 'cursos/grades/'+nome+'.html' if nome in cursos else 'errors/404.html'
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

#   @login_required
#@user_passes_test(lambda u: u.is_superuser, login_url='/error')
def usuarios(request, nome=None):
    print(request.user)
    paginas = {'editor','admin'}
    if nome is not None:
        if (nome in paginas) and request.method == 'GET':
            return render(request, 'usuarios/add'+nome+'.html')
        elif (nome in paginas) and request.method == 'POST':
            try:
                if request.POST['action'] == 'add':
                     user = User.objects.create_user(first_name=request.POST['name'], email=request.POST['email'],
                                                     username=request.POST['email'])
                     user.set_password(request.POST['key'])
                     user.is_staff = True if nome == 'editor' else False
                     user.is_superuser = True if nome == 'admin' else False
                     user.save()
                elif request.POST['action'] == 'upd':
                     user = User.objects.get(id=request.POST['control'])
                     user.first_name = request.POST['name']
                     user.email = request.POST['email']
                     user.username = request.POST['email']
                     user.set_password(request.POST['key'])
                     user.save()
                elif request.POST['action'] == 'del':
                     user = User.objects.get(id=request.POST['control'])
                     user.delete()
            except Exception as ex:
                return render(request,'errors/error.html',{'error':ex})
        else: return render(request,'errors/404.html')
    else: return render(request,'errors/404.html')


def error(request):
    return render(request,'errors/404.html')