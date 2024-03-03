from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.


def about_page(request):
    # Hämta About-objektet baserat på id
    about = About.objects.order_by('published_on').first()
    

    return render(
        request,
        "about/about.html",
        {"about": about},
    )