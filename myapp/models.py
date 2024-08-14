from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

class CustomUser(AbstractUser):
    # Example custom fields
    # birth_date = models.DateField(null=True, blank=True)
    
    # Modify the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
        blank=True,
    )

    # Modify the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        blank=True,
    )
    
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Optional: Default ordering

class contact(models.Model):
    name = models. CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models. CharField(max_length=12)
    desc = models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other relevant fields here

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    # def send_order_email(self):
    #     subject = 'Order Confirmation'
    #     message = render_to_string('order_email_template.html', {
    #         'order': self,
    #         'user': self.user
    #     })
    #     recipient_list = ['rupeshsardar@gmail.com']
        
    #     send_mail(
    #         subject,
    #         message,
    #         settings.DEFAULT_FROM_EMAIL,
    #         recipient_list,
    #         fail_silently=False,
    #     )
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    



class SupportRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"