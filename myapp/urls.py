from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import support_request
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('category_list/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('Outlet/', views.Outlet, name='Outlet'),
    path('Services/', views.Services, name='Services'),
    path('stores/', views.stores, name='stores'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('password_change/', views.password_change, name='password_change'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),
    path('support/', support_request, name='support'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
