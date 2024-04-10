from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC = Modelo Vista    Controlador -> Acciones(metodos)
# MVT = Modelo Template Vista -> Acciones(metodos)

layout = """
 <h1>Sitio web con Django | Marcos Magana </h1>
 <hr/>
 <ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
     <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
     <li>
        <a href="/pagina">Página</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
 </ul>
 <hr/>
"""

def index(request):
    html = """ 
        <h1>Inicio</h1>
        <p>Años hasta 2050: </p>
    """
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li> {year} </li>"
        year += 1

    html += "</ul>"

    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""
        <h1>Hola Mundo con Django 3.0.5!!</h1>
        <h3>Soy Marcos Magaña </h3>
    """)

def pagina(request, rediregir = 0):
    if rediregir == 1:
        #return redirect("/inicio/")
        return redirect('contacto', nombre="Marcos", apellidos="Magaña")

    return HttpResponse(layout+"""
    <h1>Página Web</h1>
    <p>Creado por Marcos Magaña</p>
""")

def contacto(request, nombre="", apellidos=""):
    html = ""

    html += "<h1>Contacto</h1>"    
    if nombre and apellidos:
        html += f"""
        <p>{nombre} {apellidos}</p>
        """
    return HttpResponse(layout+html)