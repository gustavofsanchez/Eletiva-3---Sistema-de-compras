from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from List.models import Product, Category, List, List_product
from List.models import Recipt, TagRecipt, ProductRecipt

# Create your views here.
def index(request):
    products = Product.objects.all
    lists = List.objects.all
    categories = Category.objects.all
    tagRecipts = TagRecipt.objects.all
    recipts = Recipt.objects.all
    context = {
        'prods': products,
        'lists': lists,
        'categories': categories,
        'tagRecipts': tagRecipts,
        'recipts': recipts,
    }
    return render(request, 'index.html', context)

def lists(request):
    lists = List.objects.all
    context = {
        'lists': lists,
    }
    return render(request, 'lists.html', context)


def recipes(request):
    products = Product.objects.all
    lists = List.objects.all
    categories = Category.objects.all
    tagRecipts = TagRecipt.objects.all
    recipts = Recipt.objects.all
    context = {
        'prods': products,
        'lists': lists,
        'categories': categories,
        'tagRecipts': tagRecipts,
        'recipts': recipts,
    }
    return render(request, 'recipes.html', context)

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
    return HttpResponseRedirect('/lists/')

def delete_list(request, pk):
    #if request.method == 'POST':
    list = List.objects.get(id = pk)
    list.delete()
    return HttpResponseRedirect('/lists/') 


def edit_list(request):
    if request.method == 'POST':
        list = List.objects.get(id = request.POST['id'])
        list.name = request.POST['name']
        list.save()
    return HttpResponseRedirect('/lists/') 

def add_prod_in_list(request):
    if request.method == 'POST':
        list = List.objects.get(id = request.POST['idList'])
        prod = Product.objects.get(id = request.POST['idProd'])
        quantity = request.POST['quantity']
        second_option = Product.objects.get(id = request.POST['idSecondOption'])
        importance = request.POST['importance']
        data = List_product(
            product = prod,
            list = list,
            quantity = quantity,
            product_second_option = second_option,
            importance = importance,
        )
        data.save()
    return HttpResponseRedirect('/')


def show_list(request,pk):
    list_products = List_product.objects.filter(list__id=pk)
    context = {
        'list_products': list_products,
    }
    return render(request, 'showlist.html', context)

def add_recipt(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        description = request.POST['description']
        tagCategory = TagRecipt.objects.get(id = request.POST['tagCategory'])
        data = Recipt(
            name = name,
            description = description,
            tagCategory = tagCategory
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_recipt(request, pk):
    #if request.method == 'POST':
    recipt = Recipt.objects.get(id = pk)
    recipt.delete()
    return HttpResponseRedirect('/') 

def edit_recipt(request):
    if request.method == 'POST':
        recipt = Recipt.objects.get(id = request.POST['id'])
        recipt.name = request.POST['name']
        recipt.description = request.POST['description']
        tagCategory = TagRecipt.objects.get(id = request.POST['tagCategory'])
        recipt.tagCategory = tagCategory
        recipt.save()
    return HttpResponseRedirect('/')


def add_prod_in_recipt(request):
    if request.method == 'POST':
        recipt = Recipt.objects.get(id = request.POST['idRecipt'])
        prod = Product.objects.get(id = request.POST['idProd'])
        quantity = request.POST['quantity']
        data = ProductRecipt(
            product = prod,
            recipt = recipt,
            quantity = quantity,
        )
        data.save()
    return HttpResponseRedirect('/')


def show_recipt(request,pk):
    reciptProducts = ProductRecipt.objects.filter(recipt__id=pk)
    context = {
        'reciptProducts': reciptProducts,
    }
    return render(request, 'showRecipt.html', context)