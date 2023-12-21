from django.shortcuts import render
from django.views.generic import FormView
from .forms import HouseSaleForm
# Create your views here.


class IndexView(FormView):
    template_name = "index.html"
    form_class = HouseSaleForm
