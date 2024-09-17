from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product, Reservation
from .forms import ReservationForm

# Create your views here.
def show_main(request):
    book_entries = Product.objects.all()

    products = [
        {
            'name': 'Fathul Qorib',
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
        'products': products,
        'book_entries':book_entries
    }

    return render(request, "main.html", context)

def create_reservation_entry(request):
    products = [
        {
            'name': 'Fathul Qorib',
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
    form = ReservationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'products': products,
        }
    return render(request, "create_reservation_entry.html", context)

def show_xml_by_id(request, id):
    data = Reservation.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Reservation.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Reservation.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Reservation.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")