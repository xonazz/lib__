from django.contrib import admin

from .models import Emprestimo, Leitor, Livro

admin.site.register(Livro)
admin.site.register(Leitor)
admin.site.register(Emprestimo)
