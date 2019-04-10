from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from baitu import mysql, bcrypt, jwt



ventas = Blueprint('ventas', __name__)


@ventas.route('/listarVentas', methods=['POST'])
def listarVentas():
    if request.method == 'POST':

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM publicacion')
        lista = cur.fetchall()
        mysql.connection.commit()

    return lista

@ventas.route('/crearVenta', methods=['POST'])
def crearVenta():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Vendedor = request.get_json()['vendedor']
        Precio = request.get_json()['precio']
        Foto = request.get_json()['foto']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, vendedor) VALUES (%s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor))

        cur.execute("SELECT id FROM publicacion WHERE id = (SELECT MAX(id) from publicacion)")
        Pub = str(cur.fetchone())
        Publicacion = Pub[7:len(Pub)-1]     # formateo necesario para obtener unicamente el dato "id"

        cur.execute('INSERT INTO venta (Publicacion, Precio, Vendedor) VALUES (%s, %s, %s)', (Publicacion, Precio, Vendedor))
        cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto))
        mysql.connection.commit()

    return "Venta creada"


@ventas.route('/crearSubasta', methods=['POST'])
def crearSubasta():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Vendedor = request.get_json()['vendedor']
        precio_actual = request.get_json()['precio_actual']
        precio_salida = request.get_json()['precio_salida']
        hora_limite = request.get_json()['hora_limite']
        fecha_limite = request.get_json()['fecha_limite']
        Foto = request.get_json()['foto']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor) VALUES (%s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor))

        cur.execute("SELECT id FROM publicacion WHERE id = (SELECT MAX(id) from publicacion)")
        Publicacion = cur.fetchone()

        cur.execute('INSERT INTO subasta (Publicacion, precio_actual, precio_salida, hora_limite, fecha_limite) VALUES (%s, %s, %s, %s, %s)', 
        (Publicacion, precio_actual, precio_salida, hora_limite, fecha_limite))
        cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto))
        mysql.connection.commit()

    access_token = create_access_token(identity = {'login': Login})
    result = access_token
    return result
    

@ventas.route('/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Password = request.get_json()['password']
    result = ""

    numResultados= cur.execute("SELECT * FROM usuario where Login = '" + str(Login) + "'")
    usuario = cur.fetchone()
   
    if numResultados > 0 and usuario['Password'] ==  str(Password):
        access_token = create_access_token(identity = {'login': usuario['Login']})
        result = access_token
    else:
        result = jsonify({"error":"Invalid username and password"})
    
    return result

@ventas.route('/updateUsuario', methods=['POST'])
def updateUsuario():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Nombre = request.get_json()['nombre']
    Apellidos = request.get_json()['apellidos']
    Telefono = request.get_json()['telefono']
    Email = request.get_json()['email']

    cur.execute('UPDATE usuario SET Nombre=%s, Apellidos=%s, Telefono=%s, Email=%s WHERE Login=%s', 
    (Nombre, Apellidos, Telefono, Email, Login))
    mysql.connection.commit()


    access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos,'telefono':Telefono, 'email': Email})
    result = access_token
    return result

@ventas.route("/delete", methods=['POST'])
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

 
