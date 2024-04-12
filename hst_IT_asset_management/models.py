from django.db import models
import uuid
from django.conf import settings

class LaptopStore(models.Model):
    STORAGE_TYPES = (
        ('ssd', 'SSD'),
        ('hdd', 'HDD')
    )
    LAPTOP_STATUS = (
        ('active', 'Active'),
        ('inactive', 'In Active')
    )
    laptop_name = models.CharField(max_length=100)
    internal_serial_number = models.CharField(max_length=100)
    external_serial_number = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.IntegerField('Storage in GB')
    storage_types = models.CharField(max_length=200, choices=STORAGE_TYPES, blank=True, null=True)
    ram = models.CharField(max_length=100)
    laptop_generation = models.CharField(max_length=100)
    purchaser = models.CharField(max_length=100)
    purchased_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
    laptop_status = models.CharField(max_length=200, choices=LAPTOP_STATUS, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.laptop_name

class Store(models.Model):
    ITEM_CATEGORIES = (
        ('hard_drive', 'Hard Drive'),
        ('wifi', 'Wi-Fi Equipment'),
        ('flash_disks', 'Flash Disks'),
        ('other', 'Other')
    )
    ITEM_STATUS = (
        ('active', 'Active'),
        ('inactive', 'In Active')
    )
    item_name = models.CharField(max_length=100)
    item_categories = models.CharField(max_length=200, choices=ITEM_CATEGORIES)
    item_status = models.CharField(max_length=200, choices=ITEM_STATUS)
    item_detail = models.TextField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    purchaser = models.CharField(max_length=100)
    purchased_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.item_name
    
class Allocation(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Store, on_delete=models.CASCADE)
    allocation_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.person.username} - {self.item.item_name}'
    
class LaptopAllocation(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    laptop = models.ForeignKey(LaptopStore, on_delete=models.CASCADE)
    allocation_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.person.username} - {self.laptop.laptop_name}'
    