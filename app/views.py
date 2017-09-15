from django.shortcuts import render
from django.views.generic import TemplateView
from . import utils
from .forms import AVIForm
from django.http import HttpResponse
import os
from django.utils.encoding import smart_str

# Create your views here.


class PyAvi(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        
        form = AVIForm(request.POST, request.FILES)
        if form.is_valid():
            res = form.create_avi()     

            with open("avatar.png", 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="image/png")
                response['Content-Disposition'] = 'attachmentq; filename=' + os.path.basename("avatar.png")
                response['X-Sendfile'] = smart_str("avatar.png")
                return response

        return render(request,'index.html',{"error":True})