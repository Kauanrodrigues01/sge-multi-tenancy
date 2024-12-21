from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Supplier
from django.urls import reverse_lazy
from .forms import SupplierForm

class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers/suppliers_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset.order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context
    
    
class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'suppliers/supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:suppliers_list')
    permission_required = 'suppliers.add_supplier'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'
    context_object_name = 'supplier'
    permission_required = 'suppliers.view_supplier'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context
    

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'suppliers/supplier_update.html'
    form_class = SupplierForm
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers:suppliers_list')
    permission_required = 'suppliers.change_supplier'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context
    

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_delete.html'
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers:suppliers_list')
    permission_required = 'suppliers.delete_supplier'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context
