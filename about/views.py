from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.


def about_page(about):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = About.objects.order_by('publiched_on').first()
    about = get_object_or_404(queryset, about)

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
