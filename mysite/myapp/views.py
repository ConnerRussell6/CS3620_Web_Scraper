from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)

        soup = BeautifulSoup(page.content, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_name = link.string
            Link.objects.create(address=link_address, name=link_name)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'myapp/results.html', {'data': data})


def delete(request):
    Link.objects.all().delete()
    return HttpResponseRedirect('/')