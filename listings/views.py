from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import TemplateView
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing

class ListingsView(View):
    def get(self, request):
        listings = Listing.objects.order_by('-list_date').filter(is_published=True)
        paginator = Paginator(listings, 6)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)

        context = {
            'listings': paged_listings
        }

        return render(request, 'listings/listings.html', context)
    
class ListingView(TemplateView):

    template_name = 'listings/listing.html'

    def get_context_data(self, **kwargs):
        listing_id = kwargs['listing_id']
        listing = get_object_or_404(Listing, pk=listing_id)

        context = super().get_context_data(**kwargs)
        context['listing'] = listing

        return context

class SearchView(TemplateView):
    template_name = 'listings/search.html'

    def get_context_data(self, **kwargs):

        queryset_list = Listing.objects.order_by('-list_date')

        # Keywords
        if 'keywords' in self.request.GET:
            keywords = self.request.GET['keywords']
            if keywords:
                queryset_list = queryset_list.filter(description__icontains=keywords)
        
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city:
                queryset_list = queryset_list.filter(city__iexact=city)
        
        if 'state' in self.request.GET:
            state = self.request.GET['state']
            if state:
                queryset_list = queryset_list.filter(state__iexact=state)
        
        if 'bedrooms' in self.request.GET:
            bedrooms = self.request.GET['bedrooms']
            if bedrooms:
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

        if 'price' in self.request.GET:
            price = self.request.GET['price']
            if price:
                queryset_list = queryset_list.filter(price__lte=price)

        context = super().get_context_data(**kwargs)
        context['state_choices'] = state_choices
        context['price_choices'] = price_choices
        context['bedroom_choices'] = bedroom_choices
        context['listings'] = queryset_list
        context['values'] = self.request.GET

        return context