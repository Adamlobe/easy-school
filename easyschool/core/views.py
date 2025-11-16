from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno, Professor, Turma
from .forms import AlunoForm, ProfessorForm, TurmaForm, ResponsavelInlineFormSet

def home(request):
    # renderiza o arquivo core/templates/home/index.html
    return render(request, 'home/index.html')

# LISTAR
def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, "aluno/list.html", {"alunos": alunos})


# CRIAR
def aluno_create(request):
    aluno_form = AlunoForm(request.POST or None)
    formset = ResponsavelInlineFormSet(request.POST or None)

    if aluno_form.is_valid() and formset.is_valid():
        aluno = aluno_form.save()
        formset.instance = aluno
        formset.save()
        return redirect("aluno_list")

    return render(
        request,
        "aluno/form.html",
        {"aluno_form": aluno_form, "formset": formset}
    )


# EDITAR
def aluno_update(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    aluno_form = AlunoForm(request.POST or None, instance=aluno)
    formset = ResponsavelInlineFormSet(request.POST or None, instance=aluno)

    if aluno_form.is_valid() and formset.is_valid():
        aluno_form.save()
        formset.save()
        return redirect("aluno_list")

    return render(
        request,
        "aluno/form.html",
        {"aluno_form": aluno_form, "formset": formset}
    )


# EXCLUIR
def aluno_delete(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == "POST":
        aluno.delete()
        return redirect("aluno_list")

    return render(
        request,
        "aluno/delete.html",
        {"aluno": aluno}
    )

# Professores: list / create / update / delete
def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'professor/list.html', {'professores': professores})

def professor_create(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
    return render(request, 'professor/form.html', {'professor_form': form})

def professor_update(request, pk):
    obj = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=obj)
    return render(request, 'professor/form.html', {'professor_form': form})

def professor_delete(request, pk):
    obj = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('professor_list')
    # simple confirmation page could be implemented; for now redirect on POST only
    return render(request, 'professor/confirm_delete.html', {'object': obj, 'type': 'Professor'})

# Turmas
def turma_list(request):
    turmas = Turma.objects.select_related('professor').all()
    return render(request, 'turma/list.html', {'turmas': turmas})

def turma_create(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turma_list')
    else:
        form = TurmaForm()
    return render(request, 'turma/form.html', {'turma_form': form})

def turma_update(request, pk):
    obj = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('turma_list')
    else:
        form = TurmaForm(instance=obj)
    return render(request, 'turma/form.html', {'turma_form': form, 'object': obj})

def turma_delete(request, pk):
    obj = get_object_or_404(Turma, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('turma_list')
    return render(request, 'turma/confirm_delete.html', {'object': obj, 'type': 'Turma'})
