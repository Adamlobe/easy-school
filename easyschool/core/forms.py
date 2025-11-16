from django import forms
from django.forms import inlineformset_factory
from .models import (
    Aluno, Responsavel, Professor, Turma, Disciplina,
    Aula, ResponsavelFinanceiro, PlanoFinanceiro, Mensalidade
)


# ------------------------------
#   FORMULÁRIOS PRINCIPAIS
# ------------------------------

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "status",
            "nome",
            "data_nascimento",
            "endereco",
            "alergias",
            "restricoes_alimentares",
            "medicamentos",
            "genero",
            "turma",
            "observacoes",
        ]


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = [
            "nome",
            "cpf",
            "telefone",
            "email",
            "endereco",
        ]


# ------------------------------
#   INLINE FORMSET (Aluno -> Responsáveis)
# ------------------------------

ResponsavelInlineFormSet = inlineformset_factory(
    parent_model=Aluno,
    model=Responsavel,
    form=ResponsavelForm,
    extra=2,      # 2 responsáveis por aluno
    max_num=2,
    can_delete=False
)


# ------------------------------
#   OUTROS FORMULÁRIOS
# ------------------------------

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = "__all__"


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = "__all__"


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = "__all__"


class ResponsavelFinanceiroForm(forms.ModelForm):
    class Meta:
        model = ResponsavelFinanceiro
        fields = "__all__"


class PlanoFinanceiroForm(forms.ModelForm):
    class Meta:
        model = PlanoFinanceiro
        fields = "__all__"


class MensalidadeForm(forms.ModelForm):
    class Meta:
        model = Mensalidade
        fields = "__all__"
