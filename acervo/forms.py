from django import forms

from .models import Emprestimo, Leitor, Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "isbn", "ano_publicacao", "quantidade"]


class LeitorForm(forms.ModelForm):
    class Meta:
        model = Leitor
        fields = ["nome", "serie", "telefone"]


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ["livro", "leitor", "data_emprestimo", "data_prevista", "data_devolucao"]
        widgets = {
            "data_emprestimo": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "data_prevista": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "data_devolucao": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }
