from urllib import request
from django.shortcuts import get_list_or_404, render

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    elif category_slug == 'sales':
        goods = Products.objects.filter(discount__gt=0)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    # goods = get_list_or_404(goods);

    context = {
        "title": "Floral - Каталог",
        "goods": goods,
        "slug_url": category_slug
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)
