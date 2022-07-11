# -*- coding: utf-8 -*-

Alunos = db.define_table('alunos',
	Field('nome', 'string', label = 'Nome'),
	Field('cpf', 'string', label = 'CPF'),
	Field('email', 'string', label = 'E-mail'),
	Field('telefone', 'string', label = 'Telefone/WhatsApp'),
	Field('dt_nascimento', 'date', label = 'Data de Nascimento'),
	Field('foto', 'upload', label = 'Foto')
	)

Cursos = db.define_table('cursos',
	Field('nome', 'string', label = 'Nome'),
	Field('requisito', 'list:string', label = 'Requisito'),
	Field('carga_horaria', 'integer', label = 'Carga Horária'),
	Field('valor', 'float', label = 'Valor R$')
	)

Instrutores = db.define_table('instrutores',
	Field('nome', 'string', label = 'Nome'),
	Field('email', 'string', label = 'E-mail'),
	Field('valor_hora', 'float', label = 'Valor Hora'),
	Field('formacao', 'list:string', label = 'Formação')
	)

Turmas = db.define_table('turmas',
	Field('nome', 'string', label = 'Nome'),
	Field('instrutor', 'reference instrutores', label = 'Instrutor'),
	Field('curso', 'reference cursos', label = 'Curso'),
	Field('data_inicio', 'date', label = 'Data início'),
	Field('data_final', 'date', label = 'Data final'),
	Field('carga_horaria', 'integer', label = 'Carga horária')
	)

Matriculas = db.define_table('matriculas',
	Field('turma', 'reference turmas', label = 'Turma'),
	Field('aluno', 'reference alunos', label = 'Aluno'),
	Field('data_matricula', 'datetime', label = 'Data Matrícula')
	)