from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Category
from django.urls import reverse_lazy
from .forms import CategoryForm

class CategoryListView(ListView):
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

        return queryset.order_by('id')
    
    
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories:categories_list')
    permission_required = 'categories.add_category'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'
    permission_required = 'categories.view_category'
    

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories/category_update.html'
    form_class = CategoryForm
    context_object_name = 'category'
    success_url = reverse_lazy('categories:categories_list')
    permission_required = 'categories.change_category'
    

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('categories:categories_list')
    permission_required = 'categories.delete_category'