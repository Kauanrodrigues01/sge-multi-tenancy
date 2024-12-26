from django.views.generic import ListView, CreateView, DetailView
from .models import Inflow
from django.urls import reverse_lazy
from .forms import InflowForm
from django.contrib.auth.mixins import LoginRequiredMixin

class InflowListView(LoginRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflows/inflows_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('name')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_inflow_is_active'] = 'active'
        return context


class InflowCreateView(LoginRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflows/inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflows:inflows_list')
    permission_required = 'inflows.add_inflow'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_inflow_is_active'] = 'active'
        return context


class InflowDetailView(LoginRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflows/inflow_detail.html'
    context_object_name = 'inflow'
    permission_required = 'inflows.view_inflow'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_inflow_is_active'] = 'active'
        return context