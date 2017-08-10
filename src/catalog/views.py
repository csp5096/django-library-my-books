from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
# Import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CatalogPageView(TemplateView):
    template_name = "primes/catalog.html"




