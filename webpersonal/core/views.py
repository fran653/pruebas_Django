from django.shortcuts import render, HttpResponse
#devuelve un código con una petición, un método y una respuesta (httpresponse)
#vamos a hacer una cabecera general
html_base= """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafoliosss</a></li>
    <li><a href="/contact/">uy no toques</a></li>
</ul>
"""
# Create your views here.
def home(request):
    # Render the 'home.html' template with the given context
    return render(request, 'core/home.html')
def about(request):
    return HttpResponse(html_base + '''<h2>Acerca de </h2>
        <p>Esta es la página de acerca de</p>
        <p>Por si no fuera evidente</p>          
    ''')
def portfolio(request):
    return HttpResponse(html_base + '''<h2>Portfolio</h2>     
    ''')
def contact(request):
    return HttpResponse(html_base + '''<h2>Contacto</h2><h3>johnpollón@gmail.com</h3>
    ''')
