from django.urls import path
from .views import ListingsView, ListingView, SearchView


urlpatterns = [
    path('', ListingsView.as_view(), name='listings'),
    path('<int:listing_id>', ListingView.as_view(), name='listing'),
    path('search', SearchView.as_view(), name='search'),
]