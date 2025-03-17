from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_get_view, name='login'),
    path('login/complete/', views.login_post_view, name='login_complete'),
    path('logout/', views.logout_view, name='logout'),

    path('password-reset/send/', views.password_reset_request_view, name='password_reset_request'),
    path('password-reset/reset/<uidb64>/<token>/', views.password_reset_view, name='password_reset'),
]
