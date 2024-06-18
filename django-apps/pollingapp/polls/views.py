from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def product(request):
    return HttpResponse("Hello, user . What product you need")
