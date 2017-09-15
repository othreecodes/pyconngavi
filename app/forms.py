from django import forms
from django.utils import timezone
from .utils import generate_avi
class AVIForm(forms.Form):
    bg_color = forms.CharField(max_length=50,required=False)
    txt_color = forms.CharField(max_length=50,required=False)
    intro = forms.CharField(max_length=200,required=False)
    file = forms.FileField()

    def create_avi(self):
        img = self.save_image(self.cleaned_data['file'])
        
        data ={
            "bg_color":self.cleaned_data['bg_color'] or "#000000",
            "title":self.cleaned_data['intro'] or "Pythonista",
            "fg_color":self.cleaned_data['txt_color'] or "#ffffff",
            "image": img
        }

        generate_avi(data)

        


    def save_image(self,f):  
        with open('image-'+str(timezone.now())+".png", 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            return destination