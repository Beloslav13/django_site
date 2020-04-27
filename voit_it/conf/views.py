from django.shortcuts import render

from .models import SettingsSite


# Create your views here.
def rend_logo(request):
    logos = SettingsSite.objects.all()
    return render(request, 'base.html', context={'logos': logos})
