from django.urls import path
from . import views

app_name = 'outflows'

urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflows_list'),
    path('outflows/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),
]
