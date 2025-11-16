from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Alunos
    path('alunos/', views.aluno_list, name='aluno_list'),
    path('alunos/novo/', views.aluno_create, name='aluno_create'),
    path('alunos/<int:pk>/editar/', views.aluno_update, name='aluno_update'),
    path('alunos/<int:pk>/excluir/', views.aluno_delete, name='aluno_delete'),

    # Professores
    path('professores/', views.professor_list, name='professor_list'),
    path('professores/novo/', views.professor_create, name='professor_create'),
    path('professores/<int:pk>/editar/', views.professor_update, name='professor_update'),
    path('professores/<int:pk>/excluir/', views.professor_delete, name='professor_delete'),

    # Turmas
    path('turmas/', views.turma_list, name='turma_list'),
    path('turmas/novo/', views.turma_create, name='turma_create'),
    path('turmas/<int:pk>/editar/', views.turma_update, name='turma_update'),
    path('turmas/<int:pk>/excluir/', views.turma_delete, name='turma_delete'),
]

