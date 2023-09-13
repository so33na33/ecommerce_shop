from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import category,product
# Create your views her

from django.core.paginator import Paginator,EmptyPage,InvalidPage

def allProductCat(request,cat_slug=None):

    cat_page=None
    products_list=None
    if cat_slug!=None:
        cat_page=get_object_or_404(category, slug=cat_slug)
        products_list=product.objects.all().filter(category=cat_page,available=True)
    else:
        products_list=product.objects.all().filter(available=True)
        paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(Paginator.num_pages)

    return render(request,'category.html',{'category':cat_page,'product':products})


def proDetail(request, cat_slug, product_slug,):
    try:
        products=product.objects.get(category__slug=cat_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'product.html',{'product':products})