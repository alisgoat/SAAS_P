from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request,*args,**kwargs):
    queryset = PageVisit.objects.all()
    #return HttpResponse("<h1>Hello World</h1>")
    template = "home.html"
    PageVisit.objects.create()
    return render (request, template)