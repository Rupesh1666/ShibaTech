# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    # Add custom fields if needed
    # For example:
    # birth_date = models.DateField(null=True, blank=True)
    
    # Modify the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Unique related_name for groups
        related_query_name='custom_user_group',
        blank=True,
    )

    # Modify the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Unique related_name for user_permissions
        related_query_name='custom_user_permission',
        blank=True,
    )
    def __str__(self):
        return self.name
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
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
# dfdf
class Contact(models.Model):
    name = models. CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models. CharField(max_length=12)
    desc = models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    