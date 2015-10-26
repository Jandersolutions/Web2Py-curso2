# -*- coding: utf-8 -*-
__author__ = 'janderson'

from datetime import datetime

#Criação tabelas notas
Notas = db.define_table('notas',
    Field('nota' , 'float' ,default=0 , label="Nota" ),
    Field('disciplina' , 'reference disciplinas' ,  label="Disciplinas"),
    Field('aluno' , 'reference auth_user' , notnull=True , label="Aluno"),
    Field('professor' , 'reference auth_user' , notnull=True , label="Professor")
)

Disciplinas = db.define_table('disciplinas',
    Field('nome' , notnull=True , label="Disciplina") ,
)

#Criação tabela biblioteca
Biblioteca = db.define_table('biblioteca',
    Field('arquivo' , 'upload' , notnull=True , label="Arquivo"),
    Field('professor' , 'reference auth_user' , notnull=True , label="Professor")
)

#Criação tabela Forum
Forum = db.define_table('forum',
    Field('Titulo', notnull=True , label="Titulo"),
    Field('mensagem' , 'text' , notnull=True , label="Mensagem"),
    auth.signature
)

#Criação tabela Comentarios
Comentarios = db.define_table('comentarios',
    Field('mensagem' , 'text' , notnull=True , label="Mensagem"),
    Field('postagem' , 'reference forum' , label="Postagem"),
    auth.signature
)


