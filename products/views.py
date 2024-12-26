from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from brands.models import Brand
from categories.models import Category
from .models import Product
from .forms import ProductForm
from utils.metrics import get_products_metrics
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = Product.objects.select_related('category', 'brand').all()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        
        filters = {}

        if title:
            filters['title__icontains'] = title
        if serie_number:
            filters['serie_number__icontains'] = serie_number
        if category:
            filters['category__id'] = category
        if brand:
            filters['brand__id'] = brand
            
        if filters:
            queryset = queryset.filter(**filters)

        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['page_product_is_active'] = 'active'
        context['products_metrics'] = get_products_metrics()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    permission_required = 'products.add_product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    permission_required = 'products.view_product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    permission_required = 'products.change_product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:products_list')
    permission_required = 'products.delete_product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context