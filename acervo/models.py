from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Livro(models.Model):
    titulo = models.CharField("título", max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField("ISBN", max_length=20, blank=True)
    ano_publicacao = models.PositiveIntegerField("ano de publicação", null=True, blank=True)
    quantidade = models.PositiveIntegerField("exemplares", default=1)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} — {self.autor}"

    @property
    def disponiveis(self):
        emprestados = self.emprestimos.filter(data_devolucao__isnull=True).count()
        return self.quantidade - emprestados


class Leitor(models.Model):
    SERIES = [
        ("6EF", "6º ano"),
        ("7EF", "7º ano"),
        ("8EF", "8º ano"),
        ("9EF", "9º ano"),
        ("1EM", "1º ano EM"),
        ("2EM", "2º ano EM"),
        ("3EM", "3º ano EM"),
        ("OUT", "Outro / adulto"),
    ]

    nome = models.CharField(max_length=150)
    serie = models.CharField("série", max_length=3, choices=SERIES, default="OUT")
    telefone = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "leitores"

    def __str__(self):
        return f"{self.nome} ({self.get_serie_display()})"


def prazo_padrao():
    return timezone.localdate() + timedelta(days=14)


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="emprestimos")
    leitor = models.ForeignKey(Leitor, on_delete=models.PROTECT, related_name="emprestimos")
    data_emprestimo = models.DateField("data do empréstimo", default=timezone.localdate)
    data_prevista = models.DateField("devolução prevista", default=prazo_padrao)
    data_devolucao = models.DateField("devolvido em", null=True, blank=True)

    class Meta:
        ordering = ["-data_emprestimo", "-id"]
        verbose_name = "empréstimo"

    def __str__(self):
        return f"{self.livro.titulo} → {self.leitor.nome}"

    @property
    def atrasado(self):
        return self.data_devolucao is None and self.data_prevista < timezone.localdate()

    def clean(self):
        # Só valida estoque em empréstimos novos ainda em aberto.
        if self.livro_id and not self.pk and self.data_devolucao is None:
            if self.livro.disponiveis <= 0:
                raise ValidationError("Não há exemplares disponíveis deste livro.")
        if self.data_devolucao and self.data_devolucao < self.data_emprestimo:
            raise ValidationError("A devolução não pode ser antes do empréstimo.")
