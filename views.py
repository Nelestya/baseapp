from django.shortcuts import render , get_object_or_404
from django.views import View

from .models import Application, Image
# Create your views here.

class Index_FR(View):
    application = "home"
    template_name = "baseapp/index.html"
    language = "Fr_fr"
    
    def get(self, request):
                
        header = get_object_or_404(Application, pk=self.application)
        orbit = Image.objects.filter(langue=self.language).filter(application=self.application).filter(typeimage="caroussel")
        applications = Application.objects.all()
        context = {
            'orbit': orbit,
            'applications': applications,
            'header': header
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        pass
    
    

    
    
class ReportBug(View):
    pass

class ContactUs(View):
    pass

class AboutUs(View):
    pass

class LegalInformation(View):
    pass

class PressCenter(View):
    pass

class Download(View):
    pass

class Partner(View):
    pass