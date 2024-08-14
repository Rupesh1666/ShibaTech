from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import SupportRequest
from .models import CustomUser, Category, Product, contact, OrderItem,Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price')
 

    def notify_admin(self, request, queryset):
        for product in queryset:
            try:
                send_mail(
                    'New Product Added',
                    f'A new product has been added: {product.name}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                self.message_user(request, f"An error occurred: {str(e)}")
                return
        self.message_user(request, "Notification sent to admin.")

    notify_admin.short_description = "Notify admin about selected products"

# Register models
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser)
admin.site.register(contact)
admin.site.register(OrderItem)
admin.site.register(SupportRequest)

class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date')
    search_fields = ('name', 'email', 'phone')


