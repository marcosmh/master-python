from flask import Flask,redirect, url_for, render_template
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admindba'
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)



# Context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints

@app.route('/')
def index():
    edad = 18
    personas = ['Marcos','Victor','Francisco']

    return render_template('index.html',
                           edad = edad,
                           dato1='Valor1',
                           dato2='Valor2',
                           lista=['uno','dos','tres'],
                           personas=personas
                           )

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre = None,apellidos = None):
    texto = ""
    if nombre != None and apellidos == None:
         texto = f"Bienvenido, {nombre}"

    if nombre != None and apellidos != None:
        texto =  f"Bienvenido, {nombre} {apellidos}"

    return render_template('informacion.html',texto=texto)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')


@app.route('/insertar-coche')
def insertar_coche():
    cursor = mysql.connection.cursor()
    cursor.execute(f'INSERT INTO coches VALUES (NULL,"Lambo","Gallardo",13.40,"CDMX") ')
    cursor.connection.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


