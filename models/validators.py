# -*- coding: utf-8 -*-

## Validadores de alunos
Alunos.nome.requires = IS_NOT_EMPTY()
Alunos.cpf.requires = IS_NOT_EMPTY(),IS_NOT_IN_DB(db, 'alunos.cpf')
Alunos.email.requires = IS_EMAIL(),IS_NOT_IN_DB(db, 'alunos.email')
Alunos.telefone.requires = IS_NOT_EMPTY(),IS_NOT_IN_DB(db, 'alunos.telefone')
Alunos.dt_nascimento.requires = IS_DATE(format=T('%d-%m-%Y'))
Alunos.foto.requires = IS_EMPTY_OR(IS_IMAGE(extensions=('png', 'jpeg', 'jpg'), 
									maxsize=(200, 200)))

## Validadores de cursos
Cursos.nome.requires = IS_NOT_EMPTY()
Cursos.carga_horaria.requires = IS_INT_IN_RANGE(0, 1000)
Cursos.valor.requires = IS_FLOAT_IN_RANGE(0, 9999, dot=".")

## Validadores de instrutores
Instrutores.nome.requires = IS_NOT_EMPTY()
Instrutores.email.requires = IS_EMAIL(),IS_NOT_IN_DB(db, 'instrutores.email')
Instrutores.valor_hora.requires = IS_FLOAT_IN_RANGE(0, 9999, dot=".")
Instrutores.formacao.requires = IS_NOT_EMPTY()

## Validadores de turma
Turmas.nome.requires = IS_NOT_EMPTY()
Turmas.instrutor.requires = IS_IN_DB(db, 'instrutores.id', '%(nome)s')
Turmas.curso.requires = IS_IN_DB(db, 'cursos.id', '%(nome)s')
Turmas.data_inicio.requires = IS_DATE(format=T('%d-%m-%Y'))
Turmas.data_final.requires = IS_DATE(format=T('%d-%m-%Y'))
Turmas.carga_horaria.requires = IS_INT_IN_RANGE(0, 1000)

## Validadores de matrícula
Matriculas.turma.requires = IS_IN_DB(db, 'turmas.id', '%(nome)s')
Matriculas.aluno.requires = IS_IN_DB(db, 'alunos.id', '%(nome)s')
Matriculas.data_matricula.requires = IS_DATETIME(format=T('%d-%m-%Y %H:%M:%S'))