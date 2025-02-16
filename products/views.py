from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from brands.models import Brand
from categories.models import Category
from utils.metrics import get_products_metrics
from .models import Product
from .forms import ProductForm


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = Product.objects.select_related('category', 'brand').all().filter(user=self.request.user)

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
        context['products_metrics'] = get_products_metrics(user=self.request.user)
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    permission_required = 'products.add_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    permission_required = 'products.view_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    permission_required = 'products.change_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:products_list')
    permission_required = 'products.delete_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_product_is_active'] = 'active'
        return context
