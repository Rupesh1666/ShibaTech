# urls.py
from django.urls import path
from itertools import product
from django.conf.urls.static import static
from django.conf import settings
from . import views 
from .views import category_list, product_list, product_detail, cart_add, cart_remove, cart_detail, checkout
from .views import register
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('category_list', category_list, name='category_list'),
    path('category/<int:category_id>/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart/', cart_detail, name='cart_detail'),
    path('checkout/', checkout, name='checkout'),
    path('Outlet', views.Outlet, name='Outlet'),
    path('Services', views.Services, name='Services'),
    path('stores', views.stores, name='stores'),
    # search
    path('search/', views.search, name='search'),
    path("contact", views.contact, name='contact'),
    
    
    # added
    path('product_list/<int:category_id>/', views.product_list, name='product_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 