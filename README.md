Sistema de Biblioteca Municipal
Visão geral

Aplicação web desenvolvida em Python com o framework Django para gerenciar o acervo de uma biblioteca municipal de pequeno porte (cerca de 500 livros). O sistema substitui controles manuais por um cadastro digital de livros, leitores e empréstimos, e foi pensado para rodar localmente, com a opção de salvar os dados em um banco online.

Objetivos
Organizar o acervo e saber quantos exemplares de cada livro estão disponíveis.
Cadastrar os leitores (alunos e comunidade) com a série em que estudam.
Registrar empréstimos e devoluções, identificando os atrasos.
Reunir dados no dia a dia para análises futuras, como a quantidade de livros retirados por cada série.
Funcionalidades
Livros: cadastro, edição, exclusão e busca por título, autor ou ISBN, com controle de exemplares disponíveis.
Leitores: cadastro com nome, série e telefone.
Empréstimos: registro com prazo padrão de 14 dias, botão de devolução, destaque para atrasos e bloqueio de empréstimo quando não há exemplar disponível.
Painel administrativo: acesso ao /admin do Django para gestão avançada.
Tecnologias
Python e Django (modelo MVT, com views baseadas em classes)
HTML e CSS simples, sem dependências externas
SQLite para uso local e PostgreSQL para banco online, configurável por variáveis de ambiente
