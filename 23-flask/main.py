from flask import Flask, flash, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

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


@app.route('/crear-coche',methods=['GET','POST'])
def crear_coche():
    print(request.method)

    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        print(marca," - ",modelo," - ",precio," - ",ciudad)

        cursor = mysql.connection.cursor()
        cursor.execute(f'INSERT INTO coches VALUES (NULL,%s,%s,%s,%s) ',(marca,modelo,precio,ciudad))
        cursor.connection.commit()

        flash('Se ha creado el coche correctamente.!!')
        
        return redirect(url_for('index'))

    else:
        return render_template('crear_coche.html')
    

@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches ORDER BY id DESC")
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coches.html',coches=coches)

@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s",(coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('coche.html',coche=coche[0])


@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM coches WHERE id = %s",(coche_id))
    mysql.connection.commit()

    flash('El coche ha sido eliminado.!!')

    return redirect(url_for('coches'))


@app.route('/editar-coche/<coche_id>',methods=['GET','POST'])
def editar_coche(coche_id):

    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        print(marca," - ",modelo," - ",precio," - ",ciudad)

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE coches SET
                marca = %s,
                modelo = %s,
                precio = %s,
                ciudad = %s
            WHERE id = %s
        """,(marca,modelo,precio,ciudad,coche_id))
        cursor.connection.commit()

        flash('Se ha actualizado el coche correctamente.!!')
        
        return redirect(url_for('coches'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s",(coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('crear_coche.html',coche=coche[0])




if __name__ == '__main__':
    app.run(debug=True)


