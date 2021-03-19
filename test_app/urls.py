from django.urls import path
from . import views
from .views import IndexView
from django.views.generic import TemplateView


urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name="index"),   #u indexu hocu samo formu za unos i postovanje
    path('added_item/', IndexView.as_view(template_name='added_item.html'), name="added"),  #ovo sam probao al onda dobijam na toj strani isto sto i na indexu
    #path('added_item/', TemplateView.as_view(template_name="added_item.html"), name="added" ), #ovde samo get metodu - samo prikaz liste
]
