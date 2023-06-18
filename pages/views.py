from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['realtors'] = Realtor.objects.order_by('-hire_date')
        context['mvp_realtors'] = Realtor.objects.all().filter(is_mvp=True)

        return context

class IndexView(TemplateView):

    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listings'] = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
        context['state_choices'] = state_choices
        context['price_choices'] = price_choices
        context['bedroom_choices'] = bedroom_choices

        return context
