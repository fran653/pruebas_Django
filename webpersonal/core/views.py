from django.shortcuts import render, HttpResponse
#devuelve un código con una petición, un método y una respuesta (httpresponse)
#vamos a hacer una cabecera general
# Create your views here.
def home(request):
    # Render the 'home.html' template with the given context
    return render(request, 'core/home.html')
def about(request):
    return render(request, 'core/about.html')
def portfolio(request):
    return render(request, 'core/portfolio.html')
def contact(request):
    return render(request, 'core/contact.html')
