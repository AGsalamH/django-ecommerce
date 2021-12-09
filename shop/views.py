from django.views.generic.list import ListView

from products.models import Product
# Create your views here.


class IndexPageView(ListView):
    template_name  = 'shop/index.html'
    queryset = Product.objects.all().order_by('-date_created')[:4]
    context_object_name = 'products'