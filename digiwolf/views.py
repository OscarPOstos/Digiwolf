import tempfile

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader, Template, Context
from digiwolf.functionalities.extract import extract_from_faro_de_ceuta
# from app1.tasks import add, extract_from_faro_de_ceuta
import os


def extract_page(request):
    extern_doc = loader.get_template("extract.html")
    document = extern_doc.render()
    # result = add.delay(66, 4)
    # result = extract_from_faro_de_ceuta.delay(request.GET.get('pages', 0))
    # print(result.id)

    if "pages" in request.GET:
        data = extract_from_faro_de_ceuta(request.GET.get('pages', 0))
        # f = tempfile.NamedTemporaryFile(mode="w")
        # f.name = "opiniones-politicas.json"
        # f.write(data)
        # f.seek(os.SEEK_SET)
        # print(f.name)
        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=opiniones_politicas.json'
        return response
        # f.close()

    return HttpResponse(document)


def lake_page(request):
    extern_doc = loader.get_template("lake.html")
    document = extern_doc.render()
    return HttpResponse(document)


def warehouse_page(request):
    extern_doc = loader.get_template("warehouse.html")
    document = extern_doc.render()
    return HttpResponse(document)
