from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from baitu import mysql, bcrypt, jwt



ventas = Blueprint('ventas', __name__)


@ventas.route('/listarVentas', methods=['GET'])
def listarVentas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)


@ventas.route('/crearVenta', methods=['POST'])
def crearVenta():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Precio = request.get_json()['precio']
        Foto = request.get_json()['foto']
        Vendedor = request.get_json()['vendedor']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor) VALUES (%s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor))

        cur.execute("SELECT id FROM publicacion WHERE id = (SELECT MAX(id) from publicacion)")
        Pub = str(cur.fetchone())
        Publicacion = Pub[7:len(Pub)-1]     # formateo necesario para obtener unicamente el dato "id"

        cur.execute('INSERT INTO venta (Publicacion, Precio) VALUES (%s, %s)', (Publicacion, Precio))
        cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto))
        mysql.connection.commit()

    return "Venta creada"


@ventas.route('/modificarVenta', methods=['POST'])
def modificarVenta():
    if request.method == 'POST':
        id = request.get_json()['id']
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Precio = request.get_json()['precio']
        Foto = request.get_json()['foto']


        cur = mysql.connection.cursor()
        cur.execute('UPDATE publicacion SET Nombre=%s, Descripcion=%s, Fecha=%s, Categoria=%s where id=%s',
        (Nombre, Descripcion, Fecha, Categoria, id))

        cur.execute('UPDATE fotos SET Foto=%s where publicacion=%s', (Foto, id))

        cur.execute('UPDATE venta SET Precio=%s where publicacion=%s', (Precio, id))

        mysql.connection.commit()

    return "Venta modificada"


@ventas.route('/eliminarVenta', methods=['POST'])
def eliminarVenta():
    if request.method == 'POST':
        id = request.get_json()['id']

        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM publicacion where id = '" + id + "'")

        mysql.connection.commit()

    return "Venta eliminada"

@ventas.route('/hacerOfertaVenta', methods=['POST'])
def hacerOfertaVenta():
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        venta = request.get_json()['venta']
        oferta = request.get_json()['oferta']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ofertas (usuario, venta, oferta) VALUES (%s, %s, %s)',
        (usuario, venta, oferta))

        mysql.connection.commit()

    return "Oferta realizada"

#################################################################

@ventas.route('/buscarVentaPorNombre/<Nombre>', methods=['GET'])
def buscarVentaPorNombre(Nombre):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Nombre = '" + str(Nombre) + "'")
    mysql.connection.commit()
    publicacionesPorNombre = cur.fetchall()
    return jsonify(publicacionesPorNombre)


@ventas.route("/buscarVentaPorCategoria/<Categoria>", methods=['GET'])
def buscarVentaPorCategoria(Categoria):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Categoria = '" + str(Categoria) + "'")
    mysql.connection.commit()
    publicacionesPorCategoria = cur.fetchall()
    return jsonify(publicacionesPorCategoria)


@ventas.route("/buscarVentaPorFecha/<Fecha>", methods=['GET'])
def buscarVentaPorFecha(Fecha):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Fecha = '" + str(Fecha) + "'")
    mysql.connection.commit()
    publicacionesPorFecha = cur.fetchall()
    return jsonify(publicacionesPorFecha)