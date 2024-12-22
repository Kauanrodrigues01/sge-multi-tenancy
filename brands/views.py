from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Brand
from django.urls import reverse_lazy
from .forms import BrandForm

class BrandListView(ListView):
    model = Brand
    template_name = 'brands/brands_list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset.order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_brand_is_active'] = 'active'
        return context
    
    
class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brands/brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands:brands_list')
    permission_required = 'brands.add_brand'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_brand_is_active'] = 'active'
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brands/brand_detail.html'
    context_object_name = 'brand'
    permission_required = 'brands.view_brand'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_brand_is_active'] = 'active'
        return context
    

class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'brands/brand_update.html'
    form_class = BrandForm
    context_object_name = 'brand'
    success_url = reverse_lazy('brands:brands_list')
    permission_required = 'brands.change_brand'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_brand_is_active'] = 'active'
        return context
    

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brands/brand_delete.html'
    context_object_name = 'brand'
    success_url = reverse_lazy('brands:brands_list')
    permission_required = 'brands.delete_brand'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_brand_is_active'] = 'active'
        return context