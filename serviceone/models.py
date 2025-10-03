from django.db import models
from django.conf import settings

from django.db import models

class Product(models.Model):
    INSURANCE_TYPES = [
        ("health", "Health Insurance"),
        ("life", "Life Insurance"),
        ("vehicle", "Vehicle Insurance"),
        ("property", "Property Insurance"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    insurance_type = models.CharField(max_length=20, choices=INSURANCE_TYPES)
    premium = models.DecimalField(max_digits=10, decimal_places=2)   # cost of the policy
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)  # max claimable
    duration_months = models.PositiveIntegerField()  # default duration of the policy

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.insurance_type})"

    
class Policy(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("expired", "Expired"),
        ("pending", "Pending"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="policies"
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="policies"
    )

    policy_number = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.policy_number} - {self.user.username}"

