from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from core.utils import unique_slug_generator

from accounts.mixins import StaffRequiredMixin

from .models import Product
from .forms import ProductModelForm


# Create your views here.

class ProductListView(ListView):
    template_name = 'products/product_list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'


class ProductCreateView(StaffRequiredMixin, CreateView):
    template_name = 'products/product_form.html'
    form_class = ProductModelForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = unique_slug_generator(form.instance)
        self.object = form.save()
        return super().form_valid(form)
