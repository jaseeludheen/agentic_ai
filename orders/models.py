from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Order(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("dispatched", "Dispatched"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="orders")
    product_name = models.CharField(max_length=255)  # Store product name at time of order
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    carrier = models.CharField(max_length=100, blank=True)  # Courier or delivery service
    tracking_number = models.CharField(max_length=100, blank=True)  # Tracking number
    delivery = models.TextField(blank=True)  # Address 
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product_name} ({self.status})"


class RefundRequest(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("denied", "Denied"),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="refund_requests")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="refund_requests")
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")  #get_status_display will be used to show human readable status in templates
    created_at = models.DateTimeField()


    def __str__(self):
        return f"Refund for Order #{self.order.id} - {self.status}"