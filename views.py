from django.shortcuts import render , get_object_or_404
from django.views import View

from .forms import BugReportForm
from .models import Application, Image, BugReport
# Create your views here.
class FieldsView(View):
    applications = Application.objects.all()
    fields = {
    #USE FOR HEADER
    'title': '',
    'description':'',
    'author': 'Dlugosz Tristan',
    'langue':'en',
    'meta':'',
    #END
    'message': '',
    'applications': applications,
    }

class Home(FieldsView):
    application = "home"
    template_name = "baseapp/index.html"

    def get(self, request):

        self.fields['title'] = 'home'
        self.fields['description'] = 'AMS'

        orbit = Image.objects.filter(typeimage="orbit")
        context = {
            'orbit': orbit,
            'fields': self.fields,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        pass

class ReportBug(FieldsView):
    template_name = 'baseapp/page/reportbug.html'

    def get(self, request):
        self.fields['title'] = 'Report Bug'
        self.fields['description'] = 'It\'s page for report a bug'
        form_bugreport = BugReportForm()
        context = {
        'fields': self.fields,
        'form_bugreport': form_bugreport,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form_bugreport = BugReportForm(request.POST)
        if form_bugreport.is_valid():
            try:
                cf_cleaned = form_bugreport.cleaned_data
                insert_db = BugReport.objects.create(title=cf_cleaned['title'], mail=cf_cleaned['mail'], message=cf_cleaned['message'])
                insert_db.save()
                self.fields['message'] = 'Merci pour votre contribution'

            except Exception as e:
                flag = "Exception while processing. (%s)" % e

        context = {
        'fields': self.fields,
        }


        return render(request, self.template_name, context)

class ContactUs(FieldsView):
    template_name = 'baseapp/page/contactus.html'

    def get(self, request):
        self.fields['title'] = 'Contact Us'
        self.fields['description'] = 'It\'s page for contact a humane'
        context = {
        'fields': self.fields,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass

class AboutUs(FieldsView):
    template_name = 'baseapp/page/aboutus.html'


    def get(self, request):
        self.fields['title'] = 'About Us'
        self.fields['description'] = 'AMS'
        context = {
        'fields': self.fields,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class LegalInformation(FieldsView):
    template_name = 'baseapp/page/legalinformation.html'

    def get(self, request):
        self.fields['title'] = 'Information Legal'
        self.fields['description'] = 'Page for information'
        context = {
        'fields': self.fields,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass

class PressCenter(FieldsView):
    template_name = 'baseapp/page/presscenter.html'

    def get(self, request):
        self.fields['title'] = 'Press Center'
        self.fields['description'] = 'It\'s page for the press'
        context = {
        'fields': self.fields,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass

class Partner(FieldsView):
    template_name = 'baseapp/page/partner.html'

    def get(self, request):
        self.fields['title'] = 'Partner'
        self.fields['description'] = 'It\'s page represent the partner'
        context = {
        'fields': self.fields,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass
