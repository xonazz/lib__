from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import EmprestimoForm, LeitorForm, LivroForm
from .models import Emprestimo, Leitor, Livro


class FormMixin:
    template_name = "acervo/form.html"
    titulo = ""

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["titulo"] = self.titulo
        ctx["voltar"] = self.success_url
        return ctx

    def form_valid(self, form):
        messages.success(self.request, "Salvo com sucesso.")
        return super().form_valid(form)


class ApagarMixin:
    template_name = "acervo/confirm_delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Registro removido.")
        return super().form_valid(form)


# ---------- Livros ----------
class LivroList(ListView):
    model = Livro
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(Q(titulo__icontains=q) | Q(autor__icontains=q) | Q(isbn__icontains=q))
        return qs


class LivroCreate(FormMixin, CreateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy("livro_list")
    titulo = "Novo livro"


class LivroUpdate(FormMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy("livro_list")
    titulo = "Editar livro"


class LivroDelete(ApagarMixin, DeleteView):
    model = Livro
    success_url = reverse_lazy("livro_list")


# ---------- Leitores ----------
class LeitorList(ListView):
    model = Leitor
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(nome__icontains=q)
        return qs


class LeitorCreate(FormMixin, CreateView):
    model = Leitor
    form_class = LeitorForm
    success_url = reverse_lazy("leitor_list")
    titulo = "Novo leitor"


class LeitorUpdate(FormMixin, UpdateView):
    model = Leitor
    form_class = LeitorForm
    success_url = reverse_lazy("leitor_list")
    titulo = "Editar leitor"


class LeitorDelete(ApagarMixin, DeleteView):
    model = Leitor
    success_url = reverse_lazy("leitor_list")


# ---------- Empréstimos ----------
class EmprestimoList(ListView):
    model = Emprestimo
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset().select_related("livro", "leitor")
        if self.request.GET.get("abertos"):
            qs = qs.filter(data_devolucao__isnull=True)
        return qs


class EmprestimoCreate(FormMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    success_url = reverse_lazy("emprestimo_list")
    titulo = "Novo empréstimo"


class EmprestimoUpdate(FormMixin, UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    success_url = reverse_lazy("emprestimo_list")
    titulo = "Editar empréstimo"


class EmprestimoDelete(ApagarMixin, DeleteView):
    model = Emprestimo
    success_url = reverse_lazy("emprestimo_list")


class EmprestimoDevolver(View):
    def post(self, request, pk):
        emp = get_object_or_404(Emprestimo, pk=pk)
        if emp.data_devolucao is None:
            emp.data_devolucao = timezone.localdate()
            emp.save()
            messages.success(request, "Devolução registrada.")
        return redirect("emprestimo_list")
