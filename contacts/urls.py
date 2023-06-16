from django.urls import path
from .views import ContatView

urlpatterns = [
    path('contact', ContatView.as_view(), name='contact')
]