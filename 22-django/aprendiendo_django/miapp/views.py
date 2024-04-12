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
    
    year = 2024
    hasta = range(year, 2051)
    lenguajes = ['Java','JavaScript','Python','C','C++','C#']

    return render(request, 'index.html', {
        'mi_variable': 'Soy un dato que viene de la vista',
        'nombre': 'Marcos Magaña',
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):    
    return render(request,'hola_mundo.html')


def pagina(request, rediregir = 0):
    if rediregir == 1:
        #return redirect("/inicio/")
        return redirect('contacto', nombre="Marcos", apellidos="Magaña")

    return render(request, 'pagina.html')
    

def contacto(request, nombre="", apellidos=""):
    html = "<h1>Contacto</h1>"    
    if nombre and apellidos:
        html += f"""
            <p>{nombre} {apellidos}</p>
        """
    
    return HttpResponse(layout+html)