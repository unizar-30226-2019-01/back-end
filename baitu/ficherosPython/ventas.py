from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from baitu import mysql, bcrypt, jwt, app
from random import SystemRandom
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from datetime import datetime, date, time, timedelta
import calendar

ventas = Blueprint('ventas', __name__)


@ventas.route('/listarPublicaciones', methods=['GET'])
def listarPublicaciones():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarVentas', methods=['GET'])
def listarVentas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, venta v, fotos f where p.id=v.publicacion AND p.id=f.publicacion')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarEnVenta', methods=['GET'])
def listarEnVenta():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, venta v, usuario u where p.id=v.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario="" ORDER BY p.id DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)


@ventas.route('/listarVentasMayorMenor', methods=['GET'])
def listarVentasMayorMenor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, venta v, usuario u where p.id=v.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario="" ORDER BY v.Precio DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarVentasMenorMayor', methods=['GET'])
def listarVentasMenorMayor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, venta v, usuario u where p.id=v.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario="" ORDER BY v.Precio ASC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarEnVentaDeUsuario/<login>', methods=['GET'])
def listarEnVentaDeUsuario(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, venta v, usuario u where p.id=v.publicacion AND u.Login=p.Vendedor AND p.nuevoUsuario='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarVentasAcabadas/<login>', methods=['GET'])
def listarVentasAcabadas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, venta v, usuario u where p.id=v.publicacion AND u.Login=p.Vendedor AND p.nuevoUsuario!='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)


@ventas.route('/listarProductosComprados/<login>', methods=['GET'])
def listarProductosComprados(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p where p.nuevoUsuario!='' AND p.nuevoUsuario = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)


@ventas.route('/listarSubastas', methods=['GET'])
def listarSubastas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, subasta s, usuario u where p.id=s.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario="" ORDER BY p.id DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasMayorMenor', methods=['GET'])
def listarSubastasMayorMenor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, subasta s, usuario u where p.id=s.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario="" ORDER BY s.precio_actual DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasMenorMayor', methods=['GET'])
def listarSubastasMenorMayor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, subasta s, usuario u where p.id=s.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario="" ORDER BY s.precio_actual ASC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasDeUsuario/<login>', methods=['GET'])
def listarSubastasDeUsuario(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, subasta s, usuario u where p.id=s.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasAcabadas/<login>', methods=['GET'])
def listarSubastasAcabadas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, subasta s, usuario u where p.id=s.publicacion AND p.Vendedor=u.Login AND p.nuevoUsuario!='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

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

@ventas.route('/getTipoPublicacion/<id>', methods=['GET'])
def getTipoPublicacion(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM venta v where v.publicacion=%s', (id))
    venta = cur.fetchone()

    if venta is None:
        mysql.connection.commit()
        return "Subasta"
    else:
        mysql.connection.commit()
        return "Venta"

@ventas.route('/filtrarVentas/<nombre>/<categoria>/<orden>/<precio>', methods=['GET'])
def filtrarVentas(nombre,categoria,orden,precio):
    if precio != 0 and precio != 1000:
        cadenaPrecio = " AND v.precio<=" + str(precio)
    else:
        cadenaPrecio = ""
    if nombre != "":
        cadenaNombre = " AND p.nombre='" + str(nombre) + "'"
    else:
        cadenaPrecio = ""
    cur = mysql.connection.cursor()
    if orden=='MayorAMenor':
        cur.execute("SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.categoria='" + str(categoria) + "'" + cadenaPrecio + "ORDER BY v.Precio DESC")
        lista = cur.fetchall()
    elif orden=='MenorAMayor':
        cur.execute("SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.categoria='" + str(categoria) + "'" + cadenaPrecio + "ORDER BY v.Precio ASC")
        lista = cur.fetchall()

    mysql.connection.commit()
    return jsonify(lista)

@ventas.route('/filtrarSubastas/<nombre>/<categoria>/<orden>/<precio>', methods=['GET'])
def filtrarSubastas(nombre,categoria,orden,precio):
    if precio != 0 and precio != 1000:
        cadenaPrecio = " AND s.precio_salida<=" + str(precio)
    else:
        cadenaPrecio = ""
    if nombre != "":
        cadenaNombre = " AND p.nombre='" + str(nombre) + "'"
    else:
        cadenaPrecio = ""
    cur = mysql.connection.cursor()
    if orden=='MayorAMenor':
        cur.execute("SELECT * FROM publicacion p, subasta s where p.id=v.publicacion AND p.categoria='" + str(categoria) + "'" + cadenaPrecio + "ORDER BY s.precio_salida DESC")
        lista = cur.fetchall()
    elif orden=='MenorAMayor':
        cur.execute("SELECT * FROM publicacion p, subasta s where p.id=v.publicacion AND p.categoria='" + str(categoria) + "'" + cadenaPrecio + "ORDER BY s.precio_salida ASC")
        lista = cur.fetchall()

    mysql.connection.commit()
    return jsonify(lista)

#####################################################################
########## CREAR, EDITAR, ELIMINAR

@ventas.route('/crearVenta', methods=['POST'])
def crearVenta():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Vendedor = request.get_json()['vendedor']
        Precio = request.get_json()['precio']
        FotoP = request.get_json()['fotoPrincipal']
        Foto1 = request.get_json()['foto1']
        Foto2 = request.get_json()['foto2']
        Foto3 = request.get_json()['foto3']
        Provincia  = request.get_json()['provincia']

        cur = mysql.connection.cursor()
        numeroRegistrosAfectados  = cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoPrincipal, Provincia) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoP, Provincia))

        cur.execute("SELECT id FROM publicacion WHERE id = (SELECT MAX(id) from publicacion)")
        Pub = cur.fetchone()
        Publicacion = Pub['id']

        cur.execute('INSERT INTO venta (Publicacion, Precio) VALUES (%s, %s)', (Publicacion, Precio))

        #cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, FotoP)) NO METER FOTOP EN FOTOS (guille)
        if Foto1 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto1))

        if Foto2 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto2))

        if Foto3 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto3))

        mysql.connection.commit()

        if numeroRegistrosAfectados > 0:
            return "Exito"
        else:
            return "Error"


@ventas.route('/crearSubasta', methods=['POST'])
def crearSubasta():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Vendedor = request.get_json()['vendedor']
        Precio = request.get_json()['precio']
        FechaLimite = request.get_json()['fechaLimite']
        HoraLimite = request.get_json()['horaLimite']
        FotoP = request.get_json()['fotoPrincipal']
        Foto1 = request.get_json()['foto1']
        Foto2 = request.get_json()['foto2']
        Foto3 = request.get_json()['foto3']
        Provincia  = request.get_json()['provincia']


        cur = mysql.connection.cursor()
        numeroRegistrosAfectados  = cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoPrincipal, Provincia) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoP, Provincia))

        cur.execute("SELECT id FROM publicacion WHERE id = (SELECT MAX(id) from publicacion)")
        Pub = cur.fetchone()
        Publicacion = Pub['id']

        cur.execute('INSERT INTO subasta (publicacion, precio_actual, precio_salida, hora_limite, fecha_limite) VALUES (%s, %s, %s, %s, %s)',
        (Publicacion, Precio, Precio, HoraLimite, FechaLimite))
        #cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, FotoP)) NO METER FOTOP EN FOTOS (guille)
        if Foto1 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto1))

        if Foto2 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto2))

        if Foto3 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (Publicacion, Foto3))

        mysql.connection.commit()


        lanzarThread(str(FechaLimite),str(HoraLimite),Publicacion)

        if numeroRegistrosAfectados > 0:
            return "Exito"
        else:
            return "Error"


@ventas.route('/obtenerTipoProducto/<id>', methods=['GET'])
def obtenerTipo(id):
    cur = mysql.connection.cursor()

    numRes = cur.execute("SELECT * FROM venta WHERE  publicacion = '" + id + "'")

    if numRes > 0:
        return "Venta"
    else:
        return "Subasta"


@ventas.route('/obtenerDatosVenta/<id>', methods=['GET'])
def obtenerDatosVenta(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM publicacion p, venta v WHERE p.id=v.publicacion AND p.id = '" + id + "'")
    mysql.connection.commit()
    datos = cur.fetchone()

    return jsonify(datos)



@ventas.route('/obtenerDatosSubasta/<id>', methods=['GET'])
def obtenerDatosSubasta(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, subasta s WHERE p.id=s.publicacion AND p.id = '" + id + "'")
    mysql.connection.commit()
    datos = cur.fetchone()
    return jsonify(datos)


@ventas.route('/obtenerFotos/<id>', methods=['GET'])
def obtenerFotos(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fotos f WHERE publicacion = '" + id + "'")
    fotos = cur.fetchall()
    mysql.connection.commit()

    return jsonify(fotos)


@ventas.route('/modificarVenta', methods=['POST'])
def modificarVenta():
    if request.method == 'POST':
        id = request.get_json()['idP']
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Categoria = request.get_json()['categoria']
        FotoP = request.get_json()['fotoP']
        Foto1 = request.get_json()['foto1']
        Foto2 = request.get_json()['foto2']
        Foto3 = request.get_json()['foto3']
        FotoPAntigua = request.get_json()['fotoPAntigua']
        Foto1Antigua = request.get_json()['foto1Antigua']
        Foto2Antigua = request.get_json()['foto2Antigua']
        Foto3Antigua = request.get_json()['foto3Antigua']
        Precio = request.get_json()['precio']
        Fecha = request.get_json()['fecha']


        cur = mysql.connection.cursor()
        cur.execute('UPDATE publicacion SET Nombre=%s, Descripcion=%s, Fecha=%s, Categoria=%s, FotoPrincipal=%s where id=%s',
        (Nombre, Descripcion, Fecha, Categoria, FotoP, id))

        cur.execute('UPDATE venta SET Precio=%s where publicacion=%s', (Precio, id))

        #Borrar antiguas fotos
        if Foto1Antigua != "vacio" :
            cur.execute('DELETE FROM fotos where publicacion = %s AND foto = %s', (id, Foto1Antigua))

        if Foto2Antigua != "vacio" :
            cur.execute('DELETE FROM fotos where publicacion = %s AND foto = %s', (id, Foto2Antigua))

        if Foto3Antigua != "vacio" :
            cur.execute('DELETE FROM fotos where publicacion = %s AND foto = %s', (id, Foto3Antigua))

        #Insertar nuevas fotos
        if Foto1 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (id, Foto1))

        if Foto2 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (id, Foto2))

        if Foto3 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (id, Foto3))

        mysql.connection.commit()

        return "Exito"

@ventas.route('/modificarSubasta', methods=['POST'])
def modificarSubasta():
    if request.method == 'POST':
        id = request.get_json()['idP']
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Categoria = request.get_json()['categoria']
        FotoP = request.get_json()['fotoP']
        Foto1 = request.get_json()['foto1']
        Foto2 = request.get_json()['foto2']
        Foto3 = request.get_json()['foto3']
        FotoPAntigua = request.get_json()['fotoPAntigua']
        Foto1Antigua = request.get_json()['foto1Antigua']
        Foto2Antigua = request.get_json()['foto2Antigua']
        Foto3Antigua = request.get_json()['foto3Antigua']
        Fecha = request.get_json()['fecha']


        cur = mysql.connection.cursor()
        cur.execute('UPDATE publicacion SET Nombre=%s, Descripcion=%s, Fecha=%s, Categoria=%s, FotoPrincipal=%s where id=%s',
        (Nombre, Descripcion, Fecha, Categoria, FotoP, id))

        #Borrar antiguas fotos
        if Foto1Antigua != "vacio" :
            cur.execute('DELETE FROM fotos where publicacion = %s AND foto = %s', (id, Foto1Antigua))

        if Foto2Antigua != "vacio" :
            cur.execute('DELETE FROM fotos where publicacion = %s AND foto = %s', (id, Foto2Antigua))

        if Foto3Antigua != "vacio" :
            cur.execute('DELETE FROM fotos where publicacion = %s AND foto = %s', (id, Foto3Antigua))

        #Insertar nuevas fotos
        if Foto1 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (id, Foto1))

        if Foto2 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (id, Foto2))

        if Foto3 != "vacio" :
            cur.execute('INSERT INTO fotos (Publicacion, Foto) VALUES (%s, %s)', (id, Foto3))

        mysql.connection.commit()

        return "Exito"


@ventas.route('/eliminarVenta/<id>', methods=['POST'])
def eliminarVenta(id):

    cur = mysql.connection.cursor()
    numResultados = cur.execute("DELETE FROM publicacion where id = '" + id + "'")
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}
    return jsonify({"result": result})



@ventas.route('/eliminarSubasta/<id>', methods=['POST'])
def eliminarSubasta(id):

    cur = mysql.connection.cursor()
    numResultados = cur.execute("DELETE FROM publicacion where id = '" + id + "'")
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}
    return jsonify({"result": result})


def obtenerCorreoVendedor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT Vendedor FROM publicacion where id = '" + str(id) + "'")
    mysql.connection.commit()
    Ven = cur.fetchone()
    Vendedor = Ven['Vendedor']

    cur.execute("SELECT Email FROM usuario where login = '" + str(Vendedor) + "'")
    mysql.connection.commit()
    us = cur.fetchone()
    email = us['Email']

    return email

def obtenerCorreoComprador(usuario):
    cur = mysql.connection.cursor()

    cur.execute("SELECT Email FROM usuario where login = '" + str(usuario) + "'")
    mysql.connection.commit()
    us = cur.fetchone()
    email = us['Email']

    return email


def obtenenNombrePubli(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT Nombre FROM publicacion where id = '" + str(id) + "'")
    mysql.connection.commit()
    Ven = cur.fetchone()
    nombre = Ven['Nombre']

    return nombre

def obtenerVendedor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT Vendedor FROM publicacion where id = '" + str(id) + "'")
    mysql.connection.commit()
    Ven = cur.fetchone()
    nombre = Ven['Vendedor']

    return nombre


def obtenenPrecioVenta(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT Precio FROM venta where publicacion = '" + str(id) + "'")
    mysql.connection.commit()
    Ven = cur.fetchone()
    precio = Ven['Precio']

    return precio

def obtenenPujaMaxima(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT precio_actual FROM subasta where publicacion= '" + str(id) + "'")
    mysql.connection.commit()
    Ven = cur.fetchone()
    precioActual = Ven['precio_actual']

    return precioActual


def obtenerGanador(id):
    with app.app_context():
        cur = mysql.connection.cursor()
        numResul = cur.execute("SELECT usuario FROM pujas where subasta= '" + str(id) + "' ORDER BY puja DESC")
        mysql.connection.commit()

        if numResul > 0:
            Ven = cur.fetchone()
            ganador = Ven['usuario']
            return ganador

        else:
            return "Error"



def acabarSubasta(id):
    with app.app_context():
        cur = mysql.connection.cursor()
        ganador = obtenerGanador(id)

        if ganador!="Error":
            cur.execute('UPDATE publicacion SET nuevoUsuario=%s where id=%s', (ganador, id))
            cur.execute("DELETE FROM pujas where subasta = '" + str(id) + "'")
            mysql.connection.commit()
            nombre = obtenenNombrePubli(id)
            email = obtenerCorreoVendedor(id)
            resul = enviarEmail(str(email), 'Tu producto '+ str(nombre) + ' ha obtenido comprador: ' + str(ganador) + '.', 'Subasta finalizada')
            email = obtenerCorreoUsuario(ganador)
            resul = enviarEmail(str(email), 'Has sido el ganador de la subasta del producto '+ str(nombre) + '.', 'Subasta ganada')
        else:
            nombre = obtenenNombrePubli(id)
            email = obtenerCorreoVendedor(id)
            cur.execute("DELETE FROM publicacion where id = '" + str(id) + "'")
            mysql.connection.commit()
            resul = enviarEmail(str(email), 'Tu subasta del producto '+ str(nombre) + ' no ha obtenido comprador. Se ha eliminado la subasta', 'Subasta eliminada')


        return "Puja acabada"


#########################################################################
#######    OFERTAS

@ventas.route('/hacerOfertaVenta/<id>/<precio>', methods=['POST'])
def hacerOfertaVenta(id,precio):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']

        cur = mysql.connection.cursor()
        numResultados = cur.execute("SELECT * FROM ofertas where usuario = '" + str(usuario) + "' AND venta= '" + str(id) + "'")
        if numResultados == 0:
            precioVenta = obtenenPrecioVenta(id)

            if float(precio) >= precioVenta:

                cur.execute('INSERT INTO ofertas (usuario, venta, precio) VALUES (%s, %s, %s)', (usuario, id, precio))
                mysql.connection.commit()
                email = obtenerCorreoVendedor(id)
                nombre = obtenenNombrePubli(id)
                resul = enviarEmail(str(email),'El usuario ' + usuario + ' ha realizado una oferta de ' + str(precio) + '€ por el producto '+ str(nombre)+'.', 'Han realizado una oferta')
                return "Oferta realizada"

            else:
                return "Error"

        else:
            return "Realizada"


@ventas.route('/aceptarOfertaVenta/<id>', methods=['POST'])
def aceptarOfertaVenta(id):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']

        cur = mysql.connection.cursor()
        cur.execute('UPDATE publicacion SET nuevoUsuario=%s where id=%s', (usuario, id))

        cur.execute("DELETE FROM ofertas where venta = '" + str(id) + "'")
        nombre = obtenenNombrePubli(id)
        email = obtenerCorreoComprador(usuario)

        resul = enviarEmail(str(email),'El vendedor ha aceptado tu oferta por el producto '+ str(nombre)+'.', 'Oferta aceptada')
        mysql.connection.commit()

        return "Oferta aceptada"


@ventas.route('/eliminarOfertaVenta/<id>', methods=['POST'])
def eliminarOfertaVenta(id):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        cur = mysql.connection.cursor()
        numResultados = cur.execute('DELETE FROM ofertas where venta = %s AND usuario = %s', (id, usuario))
        nombre = obtenenNombrePubli(id)
        email = obtenerCorreoComprador(usuario)

        resul = enviarEmail(str(email),'El vendedor ha rechazado tu oferta por el producto '+ str(nombre)+'.', 'Oferta rechazada')
        mysql.connection.commit()

        if numResultados > 0:
            return "Ok"
        else:
            return "Error"

@ventas.route('/eliminartodasOfertasVenta/<id>', methods=['POST'])
def eliminartodasOfertasVenta(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        numResultados = cur.execute('DELETE FROM ofertas where venta = %s', (id))
        mysql.connection.commit()

        if numResultados > 0:
            return "Ok"
        else:
            return "Error"


@ventas.route('/hacerOfertaVentaSubasta/<id>/<precio>', methods=['POST'])
def hacerOfertaVentaSubasta(id,precio):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']

        cur = mysql.connection.cursor()
        precioActual = obtenenPujaMaxima(id)

        if precioActual<float(precio):
            cur.execute('INSERT INTO pujas (usuario, subasta, puja) VALUES (%s, %s, %s)', (usuario, id, precio))
            email = obtenerCorreoVendedor(id)
            nombre = obtenenNombrePubli(id)
            resul = enviarEmail(str(email),'El usuario ' + usuario + ' ha realizado una puja de ' + str(precio) + '€ por el producto '+ str(nombre)+'.', 'Han realizado una puja')
            cur.execute('UPDATE subasta SET precio_actual=%s where publicacion=%s', (precio, id))
            mysql.connection.commit()
            return "OK"
        else:
            return "ERROR"


################ Informe negativo #################################

def obtenerCorreoUsuario(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT Email FROM usuario WHERE Login = '" +  str(login)  + "'")
    mysql.connection.commit()
    usuario = cur.fetchone()
    email= usuario['Email']

    return email


@ventas.route('/reportar/<producto>', methods=['POST'])
def reportar(producto):
    if request.method == 'POST':
        denunciante = request.get_json()['denunciante']
        vendedor= request.get_json()['vendedor']
        #tipoDenuncia= request.get_json()['tipoDenuncia']
        textoReport = request.get_json()['texto']

#Denunciante recibe correo:
        email = obtenerCorreoUsuario(denunciante)
        cuerpo= "El usuario con login \"" + vendedor + "\" ha sido reportado tras el incidente en la venta del producto \"" \
             + producto + "\" por los siguientes motivos:\n" + textoReport
        # GUTI
        # ok = enviarEmail('a.guti1417@hotmail.com','mensaje', 'Puja realizada')
        ok = enviarEmail(str(email),cuerpo, 'Tu informe negativo ha sido recibido')
#Denunciado recibe correo:
        email = obtenerCorreoUsuario(vendedor)
        cuerpo= "Has recibido un informe negativo por parte del usuario con login \"" + denunciante + \
            " debido al producto \"" + producto + "\" publicado desde tu perfil. Estos son sus motivos:\n" \
                + textoReport
        ok = enviarEmail(str(email),cuerpo, 'Informe negativo sobre ti')
#Baitu almacena la incidencia en su propio correo:
        email= 'baituenterprises@gmail.com'
        cuerpo= "Se ha recibido un informe negativo creado por el usuario con login=\"" + denunciante + \
            "\" a raíz del producto=\"" + producto + "\" vendido por el usuario=\"" + vendedor + \
                "\". La descripción de la incidencia es la siguiente:\n" + textoReport
        ok = enviarEmail(str(email),cuerpo, 'Nuevo informe negativo registrado')

        return "Reportado"

###################################################################


@ventas.route('/listarOfertas/<venta>', methods=['GET'])
def listarOfertas(venta):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ofertas where venta = '" + venta + "'")
    lista = cur.fetchall()
    mysql.connection.commit()
    return jsonify(lista)


@ventas.route('/listarPujas/<subasta>', methods=['GET'])
def listarPujas(subasta):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pujas where venta = '" + subasta + "'")
    lista = cur.fetchall()
    mysql.connection.commit()
    return jsonify(lista)



# llamar con ok = enviarEmail('a.guti1417@hotmail.com','hola', 'Puja realizada')
def enviarEmail(destinatario, msge, asunto):

        gmail_user = 'baituenterprises@gmail.com'
        gmail_password = 'vaitu1234'
        gmail_to= destinatario

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)

         # create message object instance
        msg = MIMEMultipart()
        message = msge
        # setup the parameters of the message
        msg['From'] = gmail_user
        msg['To'] = gmail_to
        msg['Subject'] = asunto

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(gmail_user, gmail_to, msg.as_string())
        server.quit()

        return "enviado"


#############################################################
####     FAVORITOS
@ventas.route('/crearFavorito/<id>', methods=['POST'])
def crearFavorito(id):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']

        cur = mysql.connection.cursor()
        numResultados = cur.execute('SELECT * FROM favoritos where (usuario=%s) AND (publicacion=%s)', (usuario, id))
        if numResultados == 0:
            cur.execute('INSERT INTO favoritos (usuario, publicacion) VALUES (%s, %s)', (usuario, id))
            mysql.connection.commit()
            return "Favorito creado"
        else:
            mysql.connection.commit()
            return "Favorito repetida"

@ventas.route('/esFavorito/<id>', methods=['POST'])
def esFavorito(id):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM favoritos where (usuario=%s) AND (publicacion=%s)', (usuario, id))
        UsuarioF = cur.fetchone()

        if UsuarioF is None:
            mysql.connection.commit()
            return "Favorito no existe"
        else:
            mysql.connection.commit()
            return "Favorito existe"


@ventas.route('/eliminarFavorito/<id>', methods=['POST'])
def eliminarFavorito(id):
    if request.method == 'POST':
        usuario = request.get_json()['usuario']
        cur = mysql.connection.cursor()
        numResultados = cur.execute('DELETE FROM favoritos where publicacion = %s AND usuario = %s', (id, usuario))
        mysql.connection.commit()
        if numResultados > 0:
            result = {'message' : 'record deleted'}
        else:
            result = {'message' : 'no record found'}
        return jsonify({"result": result})

@ventas.route('/listarVentasFavoritas/<login>', methods=['GET'])
def listarVentasFavoritas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM favoritos fav, publicacion p, venta v, usuario u where p.id=v.publicacion AND u.Login=p.Vendedor AND fav.publicacion=p.id AND fav.usuario= '" + login + "'")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasFavoritas/<login>', methods=['GET'])
def listarSubastasFavoritas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM favoritos fav, publicacion p, subasta v, usuario u where p.id=v.publicacion AND u.Login=p.Vendedor AND fav.publicacion=p.id AND fav.usuario= '" + login + "'")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

###############################################################################
def contar(fechaLimite,horaLimite,id):
    """Contar hasta un límite de tiempo"""
    nombre = threading.current_thread().getName()
    ahora = datetime.now()  # Obtiene fecha y hora actual
    horaActual = int(ahora.hour)
    minActual = int(ahora.minute)

    horaLim = int(horaLimite[0:2])
    minLim = int(horaLimite[3:5])

    fechaActual = date.today()

    print(fechaActual)
    print(fechaLimite)

    while ((str(fechaActual) < str(fechaLimite)) or (str(fechaActual) == str(fechaLimite) and (horaActual <= horaLim) and (minActual < minLim))):
        ahora = datetime.now()
        horaActual = int(ahora.hour)
        minActual = int(ahora.minute)
        fechaActual = date.today()

    print("he terminado")
    acabarSubasta(id)




def lanzarThread(fecha,hora,id):
    hilo = threading.Thread(name='hilo1',target=contar, args=(fecha,hora,id), daemon=True)
    hilo.start()



@ventas.route("/calcularValoracion/<id>/<valoracion>", methods=['POST'])
def calcularValoracion(id,valoracion):

    cur = mysql.connection.cursor()
    usuario = obtenerVendedor(id)

    cur.execute('UPDATE publicacion SET Valorado=%s where id=%s', ("SI", id))

    cur.execute("SELECT u.vecesValorado, u.sumaValoraciones FROM publicacion p, usuario u where p.Vendedor=u.Login AND p.id ='" + str(id) + "'")
    #mysql.connection.commit()
    Ven = cur.fetchone()
    vecesValorado = Ven['vecesValorado']
    sumaValoraciones = Ven['sumaValoraciones']

    print("\n\n\nENTRA en calcularValoracion con parametros:")
    print("id="+id)
    print("valoracion="+valoracion+"\n\n\n")


    vecesValorado = vecesValorado + 1
    sumaValoraciones = sumaValoraciones + float(valoracion)

    media = sumaValoraciones/vecesValorado

    cur.execute('UPDATE usuario SET Puntuacion=%s, vecesValorado=%s, sumaValoraciones=%s  where login=%s', (media,vecesValorado,sumaValoraciones,usuario))

    mysql.connection.commit()

    return "ok"
