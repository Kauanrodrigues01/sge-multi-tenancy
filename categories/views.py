from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Category
from django.urls import reverse_lazy
from .forms import CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    permission_required = 'categories.view_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset.order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category_is_active'] = 'active'
        return context


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories:categories_list')
    permission_required = 'categories.add_category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category_is_active'] = 'active'
        return context


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'
    permission_required = 'categories.view_category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category_is_active'] = 'active'
        return context


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    template_name = 'categories/category_update.html'
    form_class = CategoryForm
    context_object_name = 'category'
    success_url = reverse_lazy('categories:categories_list')
    permission_required = 'categories.change_category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category_is_active'] = 'active'
        return context


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('categories:categories_list')
    permission_required = 'categories.delete_category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category_is_active'] = 'active'
        return context