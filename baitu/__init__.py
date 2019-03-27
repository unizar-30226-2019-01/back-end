from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


mysql = MySQL()
bcrypt = Bcrypt()
jwt = JWTManager()

CORS()

def create_app():

    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'baitu'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['JWT_SECRET_KEY'] = 'secret'

    mysql.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    #from Join.ficherosPython.Actividades import act
    from baitu.ficherosPython.usuarios import users
    
    #app.register_blueprint(act)
    app.register_blueprint(users)
    

    return app