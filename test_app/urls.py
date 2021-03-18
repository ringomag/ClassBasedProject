from django.urls import path
from . import views
from .views import IndexView
from django.views.generic import TemplateView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),   #u indexu hocu samo formu za unos i postovanje
    # path('added_item.html', IndexView.as_view(), name="added"),  ovo sam probao al onda dobijam na toj strani isto sto i na indexu
    path('added_item.html', TemplateView.as_view(template_name="added_item.html"), name="added" ), #ovde samo get metodu - samo prikaz liste
]
