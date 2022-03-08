from django.shortcuts import render

from main.models import *

# Create your views here.


def indexHandler(request):
    abouts = About.objects.all()
    about_counts = AboutCount.objects.all()
    about_uss = AboutUs.objects.all()
    counts = Count.objects.all()
    return render(request, 'index.html', {'abouts':abouts,'about_counts':about_counts,'about_uss':about_uss,'counts':counts})