from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Inflow
from .forms import InflowForm


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflows/inflows_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        product = self.request.GET.get('name')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_inflow_is_active'] = 'active'
        return context


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflows/inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflows:inflows_list')
    permission_required = 'inflows.add_inflow'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_inflow_is_active'] = 'active'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflows/inflow_detail.html'
    context_object_name = 'inflow'
    permission_required = 'inflows.view_inflow'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_inflow_is_active'] = 'active'
        return context
