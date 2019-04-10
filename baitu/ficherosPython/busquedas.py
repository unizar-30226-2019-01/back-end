from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from Join import mysql, bcrypt, jwt

busqueda = Blueprint('busqueda', __name__)

##############################################################


@busqueda.route("/buscarVentaPorNombre/<nombre>", methods=['GET'])
def buscarVentaPorNombre(nombre):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Nombre = '%" + str(nombre) + "%'")
    mysql.connection.commit()
    publicacionesPorNombre = cur.fetchall()
    return jsonify(publicacionesPorNombre)


@busqueda.route("/buscarVentaPorCategoria/<categoria>", methods=['GET'])
def buscarVentaPorCategoria(categoria):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Categoria = '%" + str(categoria) + "%'")
    mysql.connection.commit()
    publicacionesPorCategoria = cur.fetchall()
    return jsonify(publicacionesPorCategoria)


@busqueda.route("/buscarVentaPorFecha/<fecha>", methods=['GET'])
def buscarVentaPorFecha(fecha):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM publicacion where Fecha = '%" + str(fecha) + "%'")
    mysql.connection.commit()
    publicacionesPorFecha = cur.fetchall()
    return jsonify(publicacionesPorFecha)
