from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
from django.template import loader
from .models import *


def index(request):
    context = {
        'messages': Product.objects.all()
    }
    return render(request, 'index.html', context)
    # template = loader.get_template('index.html')
    # context = {
    #
    # }
    # return HttpResponse(template.render(context, request))


def item(request, item_id):


    try:
        itm = Product.objects.get(Product_Id=item_id)
        message = Specification.objects.get(Product= item_id)

    except Product.DoesNotExist:
        itm = None
    context = {
        'items': itm,
        'messages': message
    }

    return render(request, 'product.html', context )



