from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from core.utils import unique_slug_generator

from accounts.mixins import StaffRequiredMixin

from .models import Product, Category
from .forms import ProductModelForm


# Create your views here.

class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.GET.get('category')
        if category and Category.objects.filter(name=category).exists():
            return queryset.filter(category__name=category)
        return queryset


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
