from django.db import models
from master.models import BaseModel, Status  # Asegúrate de importar Status
from django.contrib.auth.models import User

class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField(default=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)  # Añade este campo

    def __str__(self):
        return self.name


class PurchaseOrder(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='PurchaseOrderItem')

    def __str__(self):
        return f"Order {self.id} - {self.supplier.name}"

class PurchaseOrderItem(BaseModel):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.purchase_order}"
