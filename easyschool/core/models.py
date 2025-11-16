from django.db import models


class Responsavel(models.Model):
    aluno = models.ForeignKey(
        "Aluno",
        on_delete=models.CASCADE,
        related_name="responsaveis"
    )

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome



class Professor(models.Model):
    nome = models.CharField(max_length=150)
    apelido = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(
        Professor, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome


class Aula(models.Model):
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE)
    disciplina = models.ForeignKey("Disciplina", on_delete=models.SET_NULL, null=True, blank=True)
    professor = models.ForeignKey("Professor", on_delete=models.SET_NULL, null=True, blank=True)

    data = models.DateField()
    conteudo = models.TextField()
    atividades = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Aula {self.turma.nome} em {self.data}"


class Aluno(models.Model):
    status = models.CharField(
        max_length=20,
        choices=[("ativo", "Ativo"), ("inativo", "Inativo")],
        default="ativo"
    )

    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255, blank=True)
    data_matricula = models.DateField(auto_now_add=True)



    genero = models.CharField(
        max_length=20,
        choices=[
            ("M", "Masculino"),
            ("F", "Feminino"),
        ],
        blank=True
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    alergias = models.TextField(blank=True)
    restricoes_alimentares = models.TextField(blank=True)
    medicamentos = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class ResponsavelFinanceiro(models.Model):
    responsavel = models.ForeignKey(
        "Responsavel",
        on_delete=models.CASCADE
    )

    aluno = models.ForeignKey(
        "Aluno",
        on_delete=models.CASCADE,
        related_name="financeiro_responsavel"
    )

    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.responsavel.nome} - {self.aluno.nome}"


class PlanoFinanceiro(models.Model):
    aluno = models.OneToOneField(
        "Aluno",
        on_delete=models.CASCADE,
        related_name="plano_financeiro"
    )

    valor_mensalidade = models.DecimalField(max_digits=8, decimal_places=2)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desconto_valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    tipo_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("mensal", "Mensal"),
            ("anual", "Anual"),
        ]
    )

    modalidade = models.CharField(
        max_length=20,
        choices=[
            ("integral", "Integral"),
            ("meio_periodo", "Meio período"),
        ]
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Financeiro de {self.aluno.nome}"


class Mensalidade(models.Model):
    aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    referencia = models.CharField(max_length=20)  # Ex: "2025-01"
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    vencimento = models.DateField()
    
    pago = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True, blank=True)
    metodo_pagamento = models.CharField(
        max_length=20,
        blank=True,
        choices=[
            ("pix", "Pix"),
            ("boleto", "Boleto"),
            ("cartao", "Cartão"),
            ("dinheiro", "Dinheiro"),
        ]
    )

    def __str__(self):
        return f"{self.aluno.nome} - {self.referencia}"
