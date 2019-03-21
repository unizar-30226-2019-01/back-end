from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'baitu'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        Login = request.get_json()['login']
        Password = request.get_json()['password']
        Nombre = request.get_json()['nombre']
        Apellidos = request.get_json()['apellidos']
        Email = request.get_json()['email']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (Login, Password, Nombre, Apellidos, Email) VALUES (%s, %s, %s, %s, %s)',
        (Login, Password, Nombre, Apellidos, Email))  
        mysql.connection.commit()

    access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email})
    result = access_token
    return result
    

@app.route('/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    Password = request.get_json()['password']
    result = ""

    numResultados= cur.execute("SELECT * FROM usuarios where Login = '" + str(Login) + "'")
    usuario = cur.fetchone()
   
    if numResultados > 0 and usuario['Password'] ==  str(Password):
        access_token = create_access_token(identity = {'login': usuario['Login']})
        result = access_token
    else:
        result = jsonify({"error":"Invalid username and password"})
    
    return result

@app.route("/update/<Login>", methods=['PUT'])
def update_nombre(Login):
    cur = mysql.connection.cursor()
    Nombre = request.get_json()['Nombre']
    
    cur.execute("UPDATE usuarios SET Nombre = '" + str(Nombre) + "' where Login = " + Login)
    mysql.connection.commit()

    result = {"Nombre": title}

    return jsonify({"result": result})


@app.route("/delete", methods=['POST'])
def delete_user():
    cur = mysql.connection.cursor()
    Login = request.get_json()['login']
    numResultados = cur.execute("DELETE FROM usuarios where Login = '" + str(Login) + "'")
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}
    return jsonify({"result": result})

@app.route("/usuarios", methods=['GET'])
def usuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    return jsonify(usuarios)
    



##############################################################

@app.route('/crearVenta', methods=['POST'])
def crearActividad():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Vendedor = request.get_json()['vendedor']
        Precio = request.get_json()['precio']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO actividades (Nombre, Descripcion, Fecha, Categoria, Vendedor, Precio) VALUES (%s, %s, %s, %s, %s, %f)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor, Precio))  
        mysql.connection.commit()

    return 'create'



@app.route('/crearSubasta', methods=['POST'])
def crearActividad():
    if request.method == 'POST':
        Nombre = request.get_json()['nombre']
        Descripcion = request.get_json()['descripcion']
        Fecha = request.get_json()['fecha']
        Categoria = request.get_json()['categoria']
        Vendedor = request.get_json()['vendedor']
        Precio_actual = request.get_json()['precio_actual']
        Precio_salida = request.get_json()['precio_salida']
        Hora_limite = request.get_json()['hora_limite']
        Fecha_limite = request.get_json()['fecha_limite']


        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO actividades (Nombre, Descripcion, Fecha, Categoria, Vendedor, Precio_actual, Precio_salida, Hora_limite, Fecha_limite) VALUES (%s, %s, %s, %s, %s, %f, %f, %s, %s)',
        (Nombre, Descripcion, Fecha, Categoria, Vendedor, Precio_actual, Precio_salida, Hora_limite, Fecha_limite))  
        mysql.connection.commit()

    return 'create'



@app.route("/deleteActividad/<id>", methods=['POST'])
def delete_actividad(id):
    cur = mysql.connection.cursor()
    numResultados = cur.execute("DELETE FROM actividades where id = " + id)
    mysql.connection.commit()

    if numResultados > 0:
        result = {'message' : 'record deleted'}
    else:
        result = {'message' : 'no record found'}
    return jsonify({"result": result})


@app.route("/actividades", methods=['GET'])
def actividades():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM actividades")
    actividades = cur.fetchall()
    return jsonify(actividades)

if __name__ == '__main__':
    app.run(debug=True)