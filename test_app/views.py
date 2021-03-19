from django.shortcuts import render, redirect
from .models import Lik
from django.views import View
from .forms import *
from django.forms import ModelForm
from django.http import HttpResponseRedirect

# Create your views here.
class IndexView(View):
    form = LikForm  #ovo je forma koju uzimam po modelu
    initial = {'key': 'value'}   #inicijalne
    template_name="index.html"
    def get(self, request, *args, **kwargs):
        created = Lik.objects.all()     #ovde vucem podatke iz baze i prikazujem ih posle kroz created:created
        form = self.form(initial=self.initial)    #ovo je forma koju koristim i prikazujem kroz form:form
        return render(request, self.template_name, {"created":created,"form":form})

    def post(self, request, num=1, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('added_item/')  #ovde mozda gresim
        return render(request, self.template_name, {"form":form})    #ovde mozda gresim
