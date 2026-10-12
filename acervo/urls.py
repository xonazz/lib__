from django.urls import path
from django.views.generic import RedirectView

from . import views as v

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="livro_list"), name="home"),

    path("livros/", v.LivroList.as_view(), name="livro_list"),
    path("livros/novo/", v.LivroCreate.as_view(), name="livro_create"),
    path("livros/<int:pk>/editar/", v.LivroUpdate.as_view(), name="livro_update"),
    path("livros/<int:pk>/apagar/", v.LivroDelete.as_view(), name="livro_delete"),

    path("leitores/", v.LeitorList.as_view(), name="leitor_list"),
    path("leitores/novo/", v.LeitorCreate.as_view(), name="leitor_create"),
    path("leitores/<int:pk>/editar/", v.LeitorUpdate.as_view(), name="leitor_update"),
    path("leitores/<int:pk>/apagar/", v.LeitorDelete.as_view(), name="leitor_delete"),

    path("emprestimos/", v.EmprestimoList.as_view(), name="emprestimo_list"),
    path("emprestimos/novo/", v.EmprestimoCreate.as_view(), name="emprestimo_create"),
    path("emprestimos/<int:pk>/editar/", v.EmprestimoUpdate.as_view(), name="emprestimo_update"),
    path("emprestimos/<int:pk>/apagar/", v.EmprestimoDelete.as_view(), name="emprestimo_delete"),
    path("emprestimos/<int:pk>/devolver/", v.EmprestimoDevolver.as_view(), name="emprestimo_devolver"),
]
