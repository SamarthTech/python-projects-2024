from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

class seller_form(CreateView):
    form_class = forms.SellerForm
    success_url = reverse_lazy("home")
    template_name = "seller/seller_form.html"
