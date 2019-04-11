from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from baitu import mysql, bcrypt, jwt



users = Blueprint('users', __name__)


@users.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        Login = request.get_json()['login']
        Password = request.get_json()['password']
        Nombre = request.get_json()['nombre']
        Apellidos = request.get_json()['apellidos']
        Email = request.get_json()['email']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (Login, Password, Nombre, Apellidos, Email) VALUES (%s, %s, %s, %s, %s)',
        (Login, Password, Nombre, Apellidos, Email))  
        mysql.connection.commit()

    access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email})
    result = access_token
    return result
    

@users.route('/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Password = request.get_json()['password']
    result = ""

    numResultados= cur.execute("SELECT * FROM usuario where Login = '" + str(Login) + "'")
    usuario = cur.fetchone()
   

    if numResultados > 0 and usuario['Password'] ==  str(Password):
        access_token = create_access_token(identity = {'login': usuario['Login'], 'nombre': usuario['Nombre'], 'apellidos': usuario['Apellidos'], 'email': usuario['Email']})
        result = access_token
    else:
        result = jsonify({"error":"Invalid username and password"})
    
    return result

@users.route('/updateUsuario', methods=['POST'])
def updateUsuario():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Nombre = request.get_json()['nombre']
    Apellidos = request.get_json()['apellidos']
    Email = request.get_json()['email']

    cur.execute('UPDATE usuario SET Nombre=%s, Apellidos=%s, Email=%s WHERE Login=%s', 
    (Nombre, Apellidos, Email, Login))
    mysql.connection.commit()


    access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email})
    result = access_token
    return result

@users.route("/delete", methods=['POST'])
def delete_user():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    numResultados = cur.execute("DELETE FROM usuario where Login = '" + str(Login) + "'")
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}
    return jsonify({"result": result})

 
