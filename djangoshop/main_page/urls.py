from django.urls import path
from . import views
app_name = 'main_page'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('cloth_info', views.cloth_info, name='cloth_info'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
    name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
