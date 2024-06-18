from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from sales.models import Product
from .forms import ProductForms


# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to this app')

@csrf_exempt
def filter(request):
    val = request.POST.get('phone')
    templates = loader.get_template('index.html')
    product = Product.objects.filter(name=val)
    return HttpResponse(templates.render({'product':product}))

@csrf_exempt
def create(request):
    name = request.POST.get('name')
    color = request.POST.get('color')
    price = request.POST.get('price')
    qty = request.POST.get('qty')
    tax = request.POST.get('tax')
    total = request.POST.get('total')
    product = Product(name = name, color = color, price = price, qty = qty, tax = tax, total = total)
    product.save()
    return redirect('/')

def deletitems(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('/')

@csrf_exempt
def editrecord(request, id):
    templates = loader.get_template('edit.html')
    if request.method == 'POST':
        product = Product.objects.get(id = id)
        form = ProductForms(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        product = Product.objects.get(id = id)
        form = ProductForms(instance=product)
    return HttpResponse(templates.render({'product':product, 'form':form}))

@csrf_exempt
def add_product(request):
    templates = loader.get_template('addproduct.html')
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addproduct')      
    else:
        form = ProductForms()
        return HttpResponse(templates.render({'form':form}))
    
    
def home(request):
    templates = loader.get_template('index.html')
    val = request.GET.get('phone')
    if val != '' and val != None:
        product = Product.objects.filter(name=val)
        return HttpResponse(templates.render({'product':product}))
    else:
        product = Product.objects.all()
        return HttpResponse(templates.render({'product':product}))

def showphone(request, phone):
    value={
        'p1':phone
    }

    templates = loader.get_template('phone.html')
    return HttpResponse(templates.render(value))

@csrf_exempt
def article(request):
    value ={
        'title':request.POST.get('name'),
        'message':request.POST.get('age')
    }
    templates = loader.get_template('article.html')
    return HttpResponse(templates.render(value))

def mydashboard(request):
    templates = loader.get_template('mydashboard.html')
    return HttpResponse(templates.render())

def product(request):
    templates = loader.get_template('product.html')
    return HttpResponse(templates.render())