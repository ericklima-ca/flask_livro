# -*- coding: utf-8 -*-
# python 3.9.6

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from controller.User import UserController
from admin.Admin import start_views


config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder= 'templates')
    app.secret_key = config.SECRET
    #app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    start_views(app, db)
    db.init_app(app)


    @app.route('/')
    def index():
        return 'Tela index...'

    @app.route('/login/')
    def login():
        return 'Aqui entrará a tela de login...'

    @app.route('/login/', methods = ['POST'])
    def login_post():
        user = UserController()
        email = request.form['email']
        password = request.form['password']
        result = user.login(email, password)
        if result:
            return redirect('/admin/')
        else:
            return render_template(
                'login.html',
                data = {
                'status': 401,
                'msg': 'Dados de usuário incorretos!',
                'type': None
            })

    @app.route('/recovery_password/')
    def recovery_password():
        return 'Aqui entrará a tela de recuperação de senha...'
    
    @app.route('/recovery_password/', methods = ['POST'])
    def send_recovery_password():
        user = UserController()
        result = user.recovery(request.form['email'])
        if result:
            return render_template(
                'recovery.html',
                data = {
                    'status': 200,
                    'msg': 'E-mail de verificação enviado com sucesso!'
                }
            )
        else:
            return render_template(
                 'recovery.html',
                data = {
                    'status': 401,
                    'msg': 'Erro ao enviar e-mail de verificação!'
                }               
            )

    return app