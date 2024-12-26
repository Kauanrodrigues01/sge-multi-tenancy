from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from .forms import OutflowForm
from django.urls import reverse_lazy
from utils.metrics import get_sales_metrics
from django.contrib.auth.mixins import LoginRequiredMixin


class OutflowListView(LoginRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflows/outflows_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_outflow_is_active'] = 'active'
        context['sales_metrics'] = get_sales_metrics()
        return context


class OutflowCreateView(LoginRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflows/outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflows:outflows_list')
    permission_required = 'outflows.add_outflow'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_outflow_is_active'] = 'active'
        return context


class OutflowDetailView(LoginRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflows/outflow_detail.html'
    context_object_name = 'outflow'
    permission_required = 'outflows.view_outflow'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_outflow_is_active'] = 'active'
        return context