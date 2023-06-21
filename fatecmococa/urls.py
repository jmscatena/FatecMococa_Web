from django.urls import path
from main.views import home as home
from main.views import cursos as cursos
from main.views import institucional as institucional
from main.views import alunos as alunos
from main.views import professores as professores
urlpatterns = [
    path('', home),
    path('cursos/<str:nome>', cursos,name='cursos'),
    path('institucional/<str:nome>', institucional,name='institucional'),
    path('alunos/<str:nome>', alunos,name='alunos'),
    path('professores/<str:nome>', professores,name='professores'),
]
