from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from utils.metrics import get_sales_metrics
from .models import Outflow
from .forms import OutflowForm


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflows/outflows_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_outflow_is_active'] = 'active'
        context['sales_metrics'] = get_sales_metrics(user=self.request.user)
        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflows/outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflows:outflows_list')
    permission_required = 'outflows.add_outflow'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_outflow_is_active'] = 'active'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflows/outflow_detail.html'
    context_object_name = 'outflow'
    permission_required = 'outflows.view_outflow'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_outflow_is_active'] = 'active'
        return context
