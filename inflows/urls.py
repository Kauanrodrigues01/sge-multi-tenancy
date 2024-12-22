from django.urls import path
from . import views

app_name = 'inflows'

urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflows_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),
]
