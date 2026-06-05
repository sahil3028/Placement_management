from django.urls import path

from companies import views

app_name = 'companies'

urlpatterns = [
    path('', views.company_list_view, name='list'),
    path('create/', views.company_create_view, name='create'),
    path('<int:pk>/', views.company_detail_view, name='detail'),
    path('<int:pk>/edit/', views.company_update_view, name='update'),
    path('<int:pk>/delete/', views.company_delete_view, name='delete'),
]
