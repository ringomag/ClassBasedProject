from django.shortcuts import render, redirect
from .models import Lik
from django.views import View
from .forms import *
from django.forms import ModelForm
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
    form = LikForm
    initial = {'key': 'value'}
    template_name="index.html"
    def get(self, request, *args, **kwargs):

        created = Lik.objects.all()
        form = self.form(initial=self.initial)
        return render(request, self.template_name, {"created":created,"form":form})

    def post(self, request, *args, **kwargs):
        form = LikForm
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {"form":form})
