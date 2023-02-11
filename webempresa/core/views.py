from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
      return render(request, "core/home.html")

def about(request):
      #return HttpResponse('<h1> Acerca de </h1>')
      return render(request, "core/about.html")

def store(request):
      #return HttpResponse('<h1> Bienvenidos al tienda virtual </h1>')
      return render(request, "core/store.html")