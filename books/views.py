from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Books

class IndexView(TemplateView):

    template_name = 'books/books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context

class BookDetailView(DetailView):

    model = Books
    template_name = 'books/book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # post = Books.objects.get(slug=self.kwargs['slug'])
        context['time'] = timezone.now()
        return context