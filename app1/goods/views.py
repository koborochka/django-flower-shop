from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Floral - Каталог",
        "goods": [
            {
                "image": "deps/img/goods/kalanchoe_1.png",
                "article": "529360177",
                "name": "Каланхоэ каландива микс",
                "price": 650,
            },
            {
                "image": "deps/img/goods/kalanchoe_2.png",
                "article": "126383293",
                "name": "Каланхоэ махровый микс",
                "price": 585,
            },
            {
                "image": "deps/img/goods/kalanchoe_2.png",
                "article": "126383293",
                "name": "Каланхоэ махровый микс",
                "price": 585,
            },
            {
                "image": "deps/img/goods/kalanchoe_2.png",
                "article": "126383293",
                "name": "Каланхоэ махровый микс",
                "price": 585,
            },
            {
                "image": "deps/img/goods/kalanchoe_2.png",
                "article": "126383293",
                "name": "Каланхоэ махровый микс",
                "price": 585,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
