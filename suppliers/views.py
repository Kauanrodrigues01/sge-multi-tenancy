from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Supplier
from .forms import SupplierForm


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers/suppliers_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Supplier
    template_name = 'suppliers/supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:suppliers_list')
    permission_required = 'suppliers.add_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'
    context_object_name = 'supplier'
    permission_required = 'suppliers.view_supplier'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'suppliers/supplier_update.html'
    form_class = SupplierForm
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers:suppliers_list')
    permission_required = 'suppliers.change_supplier'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_delete.html'
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers:suppliers_list')
    permission_required = 'suppliers.delete_supplier'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_supplier_is_active'] = 'active'
        return context
