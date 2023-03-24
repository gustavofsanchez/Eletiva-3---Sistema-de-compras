from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from List.models import Product, Category, List

# Create your views here.
def index(request):
    products = Product.objects.all
    lists = List.objects.all
    categories = Category.objects.all
    context = {
        'prods': products,
        'lists': lists,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def add_product(request):
    # inserir no meu banco de dados
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = Category.objects.get(id = request.POST['category'])
        data = Product(
            name = name,
            description = description,
            category = category
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_product(request, pk):
    #if request.method == 'POST':
    prod = Product.objects.get(id = pk)
    prod.delete()
    return HttpResponseRedirect('/') 


def edit_product(request):
    if request.method == 'POST':
        prod = Product.objects.get(id = request.POST['id'])
        prod.name = request.POST['name']
        prod.description = request.POST['description']
        category = Category.objects.get(id = request.POST['category'])
        prod.category = category
        prod.save()
    return HttpResponseRedirect('/') 

def add_list(request):
    # inserir no meu banco de dados
    if request.method == 'POST':
        name = request.POST['name']
        data = List(
            name = name,
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_list(request, pk):
    #if request.method == 'POST':
    list = List.objects.get(id = pk)
    list.delete()
    return HttpResponseRedirect('/') 


def edit_list(request):
    if request.method == 'POST':
        list = List.objects.get(id = request.POST['id'])
        list.name = request.POST['name']
        list.save()
    return HttpResponseRedirect('/') 

