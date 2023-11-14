from django.urls import path
from main.views import *
from news.views import *

urlpatterns = [
    path('', home),
    path('cursos/<str:nome>', cursos,name='cursos'),
    path('institucional/<str:nome>', institucional,name='institucional'),
    path('alunos/<str:nome>', alunos,name='alunos'),
    path('professores/<str:nome>', professores,name='professores'),
    path('noticias/', index,name='news_index'),
    path('noticias/<int:pk>', index),
    path('noticias/edit/', edit,name='news_edit'),


]
