from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = [
        {
            'name': 'Fathul qorib',
            'price': 20000,
            'description': 'Kitab fiqh classic yang membahas secara mendasar terkait fiqh madzhab imam syafi\'i.'
        },
        {
            'name': 'I\'anatut tholibin',
            'price': 460000,
            'description': 'berikut adalah kitab karya imam abu bakar syatho ad dimyathi, kitab ini terdiri dari 4 jilid yang merupakan syarh dari kitab fathul mu\'in.'
        },
        {
            'name': 'Is\'adur rofiq',
            'price': 35000,
            'description': 'Kitab yang berisi tentang hukum-hukum fiqh yang disertai dengan ilmu tasawwuf..'
        },
        {
            'name': 'Siroh nabawiyah',
            'price': 150000,
            'description': 'Kitab yang berisi tentang sejarah yang berfokus pada hukum-hukum fiqh dimasa kenabian dan setelahnya.'
        },
        {
            'name': 'Shohih bukhori',
            'price': 560000,
            'description': 'Kitab yang berisi kumpulan hadits-hadits.'
        },
        {
            'name': 'Shohih muslim',
            'price': 230000,
            'description': 'Kitab yang berisi kumpulan hadits-hadits.'
        },
        {
            'name': 'Idhohul mubham',
            'price': 15000,
            'description': 'Kitab yang berisi tentang ilmu manthiq.'
        }
        # kalo mau tambah produk disini
    ]
    context = {
        'sambutan': 'Selamat Datang di ManhajBooks!',
        'slogan': 'Toko buku online terpercaya untuk kebutuhan ilmu agama Anda.', 
        'products': products
    }

    return render(request, "main.html", context)