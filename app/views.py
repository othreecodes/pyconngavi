from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class PyAvi(TemplateView):
    template_name = 'index.html'

    def post(self,request,*args,**kwargs):
        
        return ""
        