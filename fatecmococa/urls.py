from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from main.views import *
from news.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('acesso/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cursos/<str:nome>', cursos,name='cursos'),
    path('cursos/grade/<str:nome>', grades, name='grades'),

    path('institucional/<str:nome>', institucional,name='institucional'),
    path('alunos/<str:nome>', alunos,name='alunos'),
    path('professores/<str:nome>', professores,name='professores'),
    path('noticias/', index,name='news_404'),
    path('noticias/edit/', index,name='news_index'),
    path('noticias/edit/<int:pk>', index,name='news_index'),
    path('noticias/<int:pk>', index, name='news_show'),
    path('noticias/add/', editor,name='news_edit'),
    path('usuarios/<str:nome>', usuarios,name='users_add'),
    path('usuarios/', usuarios,name='users_manage'),
    path('accounts/login/', error,name='404'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
