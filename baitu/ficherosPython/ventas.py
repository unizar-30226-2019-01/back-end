from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from baitu import mysql, bcrypt, jwt
from random import SystemRandom
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ventas = Blueprint('ventas', __name__)


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
    cur.execute('SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.nuevoUsuario="" ORDER BY p.id DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)


@ventas.route('/listarVentasMayorMenor', methods=['GET'])
def listarVentasMayorMenor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.nuevoUsuario="" ORDER BY v.Precio DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarVentasMenorMayor', methods=['GET'])
def listarVentasMenorMayor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.nuevoUsuario="" ORDER BY v.Precio ASC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarEnVentaDeUsuario/<login>', methods=['GET'])
def listarEnVentaDeUsuario(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.nuevoUsuario='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarVentasAcabadas/<login>', methods=['GET'])
def listarVentasAcabadas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, venta v where p.id=v.publicacion AND p.nuevoUsuario!='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastas', methods=['GET'])
def listarSubastas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, subasta s where p.id=s.publicacion AND p.nuevoUsuario="" ORDER BY p.id DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasMayorMenor', methods=['GET'])
def listarSubastasMayorMenor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, subasta s where p.id=s.publicacion  ORDER BY s.precio_actual DESC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasMenorMayor', methods=['GET'])
def listarSubastasMenorMayor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM publicacion p, subasta s where p.id=s.publicacion ORDER BY s.precio_actual ASC')
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasDeUsuario/<login>', methods=['GET'])
def listarSubastasDeUsuario(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, subasta s where p.id=s.publicacion AND p.nuevoUsuario='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasAcabadas/<login>', methods=['GET'])
def listarSubastasAcabadas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, subasta s where p.id=s.publicacion  AND p.nuevoUsuario!='' AND p.vendedor = '" + login + "' ORDER BY p.id DESC")
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
        FotoP = request.get_json()['fotoPrincipal']
        Foto1 = request.get_json()['foto1']
        Foto2 = request.get_json()['foto2']
        Foto3 = request.get_json()['foto3']

        cur = mysql.connection.cursor()
        numeroRegistrosAfectados  = cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoPrincipal) VALUES (%s, %s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoP))

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


        cur = mysql.connection.cursor()
        numeroRegistrosAfectados  = cur.execute('INSERT INTO publicacion (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoPrincipal) VALUES (%s, %s, %s, %s, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor, FotoP))

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

        if numeroRegistrosAfectados > 0:
            return "Exito"
        else:
            return "Error"


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

#Dado un id, obtener la tabla de la venta
@ventas.route("/obtenerDatosVenta/<id>", methods=['GET'])
def obtenerDatosVenta(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, venta v, fotos f where p.id=v.Publicacion AND p.id=f.Publicacion AND v.Publicacion = '" + str(id) + "'")
    datosVenta = cur.fetchall()
    mysql.connection.commit()
    return jsonify(datosVenta)


@ventas.route("/obtenerDatosSubasta/<id>", methods=['GET'])
def obtenerDatosSubasta(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion p, subasta s, fotos f where p.id=s.Publicacion AND p.id=f.Publicacion AND s.Publicacion = '" + str(id) + "'")
    datosVenta = cur.fetchall()
    mysql.connection.commit()
    return jsonify(datosVenta)


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
    cur.execute("SELECT * FROM favoritos fav, publicacion p, venta v where p.id=v.publicacion AND fav.publicacion=p.id AND fav.usuario= '" + login + "'")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)

@ventas.route('/listarSubastasFavoritas/<login>', methods=['GET'])
def listarSubastasFavoritas(login):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM favoritos fav, publicacion p, subasta v where p.id=v.publicacion AND fav.publicacion=p.id AND fav.usuario= '" + login + "'")
    lista = cur.fetchall()
    mysql.connection.commit()

    return jsonify(lista)
