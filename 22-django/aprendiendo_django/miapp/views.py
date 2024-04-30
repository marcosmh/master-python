from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

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

    return render(request, 'pagina.html',{
        'texto': 'XXXX',
        'lista': ['Java','Python','C#']
    })
    

def contacto(request, nombre="", apellidos=""):
    html = "<h1>Contacto</h1>"    
    if nombre and apellidos:
        html += f"""
            <p>{nombre} {apellidos}</p>
        """
    
    return HttpResponse(layout+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public =  public        
    )
    articulo.save()

    return HttpResponse(f"Usuario creado.  {articulo.title} - {articulo.content} ")

def articulo(request):
    articulo = None
    response = None
    
    try:
        """
        Article.objects.get(pk=1)
        """
        articulo = Article.objects.get(title="Primer articulo!!", public=True)
        response = f"Articulo: {articulo.id}.- {articulo.title}"
    except:
        response = f"<strong>Articulo No encontrado.</strong>"


    return HttpResponse(response)

def actualizar_articulo(request,id):
    response = None
    articulo = None

    try:
        articulo = Article.objects.get(pk=id)
        articulo.title = "Terminador 1"
        articulo.content = "Pelicula de 1987"
        articulo.save()
        response = f"Articulo Actualizado. : {articulo.id}.- {articulo.title}"

    except:
        response = f"<strong>No se pudo actualizar el articulo.</strong>"
    
    return HttpResponse(response)


"""
Ejemplos de consultas en django:
        articulos = Article.objects.filter(title='MadMax', id=7)
        articulos = Article.objects.filter(title__contains = "Game")
        articulos = Article.objects.filter(title__iexact = "MadMax")
        articulos = Article.objects.filter(title__exact = "MadMax")
        
        articulos = Article.objects.filter(id__gt = 3)
        articulos = Article.objects.filter(id__gte = 3)
        articulos = Article.objects.filter(id__lt = 3)
        articulos = Article.objects.filter(id__lte = 3)
        articulos = Article.objects.filter(id__lte = 3, title__contains="Game")
        articulos = Article.objects.filter(
             title="Terminador 2",             
         ).exclude(
             public=True
         )

         articulos = Article.objects.raw(
             "SELECT * FROM miapp_article"
         )

         articulos = Article.objects.raw(
            "SELECT * FROM miapp_article WHERE public = 0 "
         )
"""
def articulos(request):
    response = None
    articulos = None
    try:
        articulos = Article.objects.all().order_by('id')        
         
    except:
        response = f"<strong>No se encontraron registros.</strong>"
    
    return render(request, 'articulos.html',{
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = None
    response = None
    try:
        articulo = Article.objects.get(pk=id)
        articulo.delete()
        return redirect('articulos')
    except:
        response = f"<strong>Error al borrar al articulos.</strong>"

    return HttpResponse(response)