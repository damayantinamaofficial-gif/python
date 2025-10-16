from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fashion','FASHION'),
        ('shoes','SHOES')
    ]
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    is_avaiable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    