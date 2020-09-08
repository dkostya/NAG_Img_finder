from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.db.models import Q
from django.template import Context, loader
from django.http import HttpResponse

from .models import Product

# Create your views here.

def index(request):
    return render(request, 'index.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})



class SearchResultsView(ListView):
    model = Product
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(sku__icontains=query)
        )
        return object_list


