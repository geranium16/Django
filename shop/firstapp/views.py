from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop


def show(request):
    shop_list = Shop.objects.all()
    html = ''
    return  render(request, 'firstapp/show.html', {"shop_list":shop_list})