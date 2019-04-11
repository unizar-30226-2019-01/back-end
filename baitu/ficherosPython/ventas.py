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
    cur.execute('SELECT * FROM publicacion p, venta v, fotos f where p.id=v.publicacion AND p.id=f.publicacion')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/obtenerVendedor', methods=['GET'])
def obtenerVendedor():
    id = request.get_json()['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT Vendedor FROM publicacion WHERE id = %s", [id])
    u = cur.fetchone()
    Usuario = u['Vendedor']
    mysql.connection.commit()

    return Usuario


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
        cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor) VALUES (%s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor))

        cur.execute("SELECT id FROM publicacion WHERE id = (SELECT MAX(id) from publicacion)")
        Pub = cur.fetchone()
        Publicacion = Pub['id']

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


@ventas.route('/hacerOfertaVenta', methods=['POST'])
def hacerOfertaVenta():
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        venta = request.get_json()['venta']

        cur = mysql.connection.cursor()
        numResultados = cur.execute('SELECT * FROM ofertas where (usuario=%s) AND (venta=%s)', (usuario, venta))
        if numResultados == 0:
            cur.execute('INSERT INTO ofertas (usuario, venta) VALUES (%s, %s)', (usuario, venta))
            mysql.connection.commit()
            return "Oferta realizada"
        else:
            mysql.connection.commit()
            return "Oferta repetida"


@ventas.route('/eliminarVenta', methods=['POST'])
def eliminarVenta():
    cur = mysql.connection.cursor()
    id = request.get_json()['id']
    numResultados = cur.execute('DELETE FROM publicacion where id = %s', [id])
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}
    return jsonify({"result": result})


@ventas.route('/aceptarOfertaVenta', methods=['POST'])
def aceptarOfertaVenta():
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        venta = request.get_json()['venta']

        cur = mysql.connection.cursor()
        cur.execute('UPDATE publicacion SET nuevoUsuario=%s where id=%s', (usuario, venta))

        cur.execute("DELETE FROM ofertas where venta = '" + venta + "'")

        mysql.connection.commit()

    return "Oferta aceptada"


@ventas.route('/eliminarOfertaVenta', methods=['POST'])
def eliminarOfertaVenta():
    if request.method == 'POST':
        venta = request.get_json()['venta']
        usuario = request.get_json()['usuario']
        cur = mysql.connection.cursor()
        numResultados = cur.execute('DELETE FROM ofertas where venta = %s AND usuario = %s', (venta, usuario))
        mysql.connection.commit()

        if numResultados > 0:
            result = {'message' : 'record deleted'}
        else:
            result = {'message' : 'no record found'}
        return jsonify({"result": result})


@ventas.route('/listarOfertas/<venta>', methods=['GET'])
def listarOfertas(venta):
    cur = mysql.connection.cursor()
    cur.execute("SELECT usuario FROM ofertas where venta = '" + venta + "'")
    lista = cur.fetchall()
    mysql.connection.commit()
    return jsonify(lista)


@ventas.route('/buscarVentaPorNombre/<Nombre>', methods=['GET'])
def buscarVentaPorNombre(Nombre):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Nombre = '" + str(Nombre) + "'")
    publicacionesPorNombre = cur.fetchall()
    mysql.connection.commit()
    return jsonify(publicacionesPorNombre)


@ventas.route("/buscarVentaPorCategoria/<Categoria>", methods=['GET'])
def buscarVentaPorCategoria(Categoria):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Categoria = '" + str(Categoria) + "'")
    publicacionesPorCategoria = cur.fetchall()
    mysql.connection.commit()
    return jsonify(publicacionesPorCategoria)


@ventas.route("/buscarVentaPorFecha/<Fecha>", methods=['GET'])
def buscarVentaPorFecha(Fecha):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Fecha = '" + str(Fecha) + "'")
    publicacionesPorFecha = cur.fetchall()
    mysql.connection.commit()
    return jsonify(publicacionesPorFecha)

#Dado un id, obtener la tabla de la venta
@ventas.route("/obtenerDatosVenta/<id>", methods=['GET'])
def obtenerDatosVenta(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM venta where Publicacion = '" + str(id) + "'")
    datosVenta = cur.fetchall()
    mysql.connection.commit()
    return jsonify(datosVenta)


@ventas.route("/obtenerDatosSubasta/<id>", methods=['GET'])
def obtenerDatosSubasta(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM subasta where Publicacion = '" + id + "'")
    datosSubasta = cur.fetchall()
    mysql.connection.commit()
    return jsonify(datosSubasta)

@ventas.route('/crearFavorito', methods=['POST'])
def crearFavorito():
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        publicacion = request.get_json()['publicacion']

        cur = mysql.connection.cursor()
        numResultados = cur.execute('SELECT * FROM favoritos where (usuario=%s) AND (publicacion=%s)', (usuario, publicacion))
        if numResultados == 0:
            cur.execute('INSERT INTO favoritos (usuario, publicacion) VALUES (%s, %s)', (usuario, publicacion))
            mysql.connection.commit()
            return "Favorito creado"
        else:
            mysql.connection.commit()
            return "Favorito repetida"


@ventas.route('/eliminarFavorito', methods=['POST'])
def eliminarFavorito():
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        publicacion = request.get_json()['publicacion']
        cur = mysql.connection.cursor()
        numResultados = cur.execute('DELETE FROM favoritos where publicacion = %s AND usuario = %s', (publicacion, usuario))
        mysql.connection.commit()

        if numResultados > 0:
            result = {'message' : 'record deleted'}
        else:
            result = {'message' : 'no record found'}
        return jsonify({"result": result})
