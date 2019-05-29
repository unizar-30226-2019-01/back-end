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
        Foto = request.get_json()['foto']
        Telefono = request.get_json()['telefono']

        try:
            cur = mysql.connection.cursor()
            resultado =cur.execute('INSERT INTO usuario (Login, Password, Nombre, Apellidos, Email, Foto, Telefono) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (Login, Password, Nombre, Apellidos, Email, Foto, Telefono))
            mysql.connection.commit()

            access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email, 'foto': Foto})
            result = access_token
            return result

        except:

            return "Error"

@users.route('/registerCheck', methods=['POST'])
def registerCheck():
    if request.method == 'POST':
        Login = request.get_json()['login']
        Password = request.get_json()['password']
        Nombre = request.get_json()['nombre']
        Apellidos = request.get_json()['apellidos']
        Email = request.get_json()['email']
        Foto = request.get_json()['foto']
        Telefono = request.get_json()['telefono']

        try:
            cur = mysql.connection.cursor()
            resultado =cur.execute('INSERT INTO usuario (Login, Password, Nombre, Apellidos, Email, Foto, Telefono) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (Login, Password, Nombre, Apellidos, Email, Foto, Telefono))
            mysql.connection.commit()

            return "exito"

        except:

            return "error"

@users.route('/loginCheck', methods=['POST'])
def loginCheck():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Password = request.get_json()['password']
    result = ""

    numResultados= cur.execute("SELECT * FROM usuario where Login = '" + str(Login) + "'")
    usuario = cur.fetchone()


    if numResultados > 0 and usuario['Password'] ==  str(Password):
        result = "exito"
    else:
        result = "error"
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
        access_token = create_access_token(identity = {'login': usuario['Login'], 'nombre': usuario['Nombre'], 'apellidos': usuario['Apellidos'], 'email': usuario['Email'], 'foto': usuario['Foto']})
        result = access_token
    else:
        result = "Error"

    return result

@users.route('/updateUsuario', methods=['POST'])
def updateUsuario():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Nombre = request.get_json()['nombre']
    Apellidos = request.get_json()['apellidos']
    Email = request.get_json()['email']
    Telefono = request.get_json()['telefono']
    Foto = request.get_json()['foto']
    
    cur.execute('UPDATE usuario SET Nombre=%s, Apellidos=%s, Email=%s, Telefono=%s, Foto=%s WHERE Login=%s',
    (Nombre, Apellidos, Email, Telefono, Foto, Login))
    mysql.connection.commit()


    access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email})
    result = access_token
    return result

@users.route('/updateUsuarioFoto', methods=['POST'])
def updateUsuarioFoto():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Foto = request.get_json()['foto']

    cur.execute('UPDATE usuario SET Foto=%s WHERE Login=%s',(Foto, Login))
    mysql.connection.commit()

    return "ok"


@users.route("/delete", methods=['POST'])
def delete_user():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']

    #Elimina los productos en venta del usuario:                             Esto es para que pille bien la publicacion, sino se SQL se ralla
    cur.execute("DELETE FROM publicacion WHERE vendedor='" + str(Login) + "' AND nuevoUsuario=''")
    #cur.execute("DELETE FROM publicacion WHERE id IN (SELECT v.Publicacion FROM (select * from publicacion)p, venta v, usuario u where p.id=v.publicacion AND u.Login=p.Vendedor AND p.nuevoUsuario='' AND p.vendedor = '" + str(Login) + "')")

    numResultados = cur.execute("DELETE FROM usuario where Login = '" + str(Login) + "'")
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}

    return jsonify({"result": result})

@users.route("/tieneSub", methods=['POST'])
def tieneSub():
    cur = mysql.connection.cursor()
    login = request.get_json()['login']

    numResultados=cur.execute("SELECT * FROM subasta s, publicacion p where s.publicacion=p.id AND p.Vendedor= '"+ str(login) + "'")
    mysql.connection.commit()

    if numResultados > 0:
        return "SI"
    else:
        return "NO"


@users.route("/infoUsuario", methods=['POST'])
def infoActividad():

    login = request.get_json()['usuario']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario WHERE Login = '" +  login  + "'")
    mysql.connection.commit()
    usuario = cur.fetchone()
    return jsonify(usuario)
