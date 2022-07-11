# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
@auth.requires_login()
def index():
    #response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

# Cadastro de aluno
@auth.requires_login()
def novo_aluno():
    form = SQLFORM(Alunos)
    if form.process().accepted:
        session.flash = 'Novo aluno cadastrado: %s' % form.vars.nome
        redirect(URL('novo_aluno'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# Cadastro de curso
@auth.requires_login()
def novo_curso():
    form = SQLFORM(Cursos)
    if form.process().accepted:
        session.flash = 'Novo curso cadastrado: %s' % form.vars.nome
        redirect(URL('novo_curso'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# Cadastro de instrutor
@auth.requires_login()
def novo_instrutor():
    form = SQLFORM(Instrutores)
    if form.process().accepted:
        session.flash = 'Novo instrutor cadastrado: %s' % form.vars.nome
        redirect(URL('novo_curso'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# Cadastro de turma
@auth.requires_login()
def nova_turma():
    form = SQLFORM(Turmas)
    if form.process().accepted:
        session.flash = 'Nova turma cadastrada: %s' % form.vars.nome
        redirect(URL('nova_turma'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# Cadastro de matrícula
@auth.requires_login()
def nova_matricula():
    form = SQLFORM(Matriculas)
    if form.process().accepted:
        session.flash = 'Nova matrícula cadastrada.'
        redirect(URL('nova_matricula'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

## Listagens

# Listagem de alunos
@auth.requires_login()
def lista_alunos():
    grid = SQLFORM.grid(Alunos)
    return dict(grid=grid)

# Listagem de cursos
@auth.requires_login()
def lista_cursos():
    grid = SQLFORM.grid(Cursos)
    return dict(grid=grid)

# Listagem de instrutores
@auth.requires_login()
def lista_instrutores():
    grid = SQLFORM.grid(Instrutores)
    return dict(grid=grid)

# Listagem de turmas
@auth.requires_login()
def lista_turmas():
    grid = SQLFORM.grid(Turmas)
    return dict(grid=grid)

# Listagem de matriculas
@auth.requires_login()
def lista_matriculas():
    grid = SQLFORM.grid(Matriculas)
    return dict(grid=grid)
