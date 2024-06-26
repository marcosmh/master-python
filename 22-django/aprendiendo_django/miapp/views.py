from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

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

         articulos = Article.objects.filter(
            Q(title__contains="MadMax") | Q(title__contains="Iron Man")
        )
"""
def articulos(request):
    response = None
    articulos = None
    try:
        articulos = Article.objects.all().order_by('id')        
        response = articulos
         
    except:
        response = f"<strong>No se encontraron registros.</strong>"
    
    return render(request, 'articulos.html',{
        'articulos': response
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

def save_article(request):
    mensaje = None
    try:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            public = request.POST['public']

            articulo = Article(
                title = title,
                content = content,
                public =  public        
            )
            articulo.save()
            mensaje = f"Usuario creado.  {articulo.title} - {articulo.content} "
        else:
            mensaje = f"<h2> Error al crear el Articulo</h2>"
    except Exception as e:
        mensaje = "Ha ocurrido un error ", type(e).__name__
        print(mensaje)


    return HttpResponse(mensaje)

def create_article(request):
    return render(request, 'create_article.html')



def create_full_article(request):
        
    if request.method == 'POST':
        try:
            formulario = FormArticle(request.POST)   
            if formulario.is_valid():     
                data_form = formulario.cleaned_data
                title   = data_form.get('title')
                content = data_form['content']
                public  = data_form['public']
                print(title +' - '+ content +' - '+public)
                articulo = Article(
                        title   = title,
                        content = content,
                        public  = public
                    )
                articulo.save()

                # crear mensaje flash
                messages.success(request,f'Se ha guardado el Articulo. ID= {articulo.id}')
                return redirect('articulos')            
        except Exception as e:
            mensaje = "Exception: -> Ha ocurrido un error: ", type(e).__name__
            print(e)
            print(mensaje)            
    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
            'form': formulario
        })