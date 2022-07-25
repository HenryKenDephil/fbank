from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    #introducing choices
    PRODUCT_CHOICES = (
        ('ELECTRONICS', 'Electronics'),
        ('COMPUTERS', 'Computers'),
        ('PHONES', 'Phones'),
        ('LAND', 'Land'),
        ('HOUSING', 'Housing'),
        ('VEHICLES', 'Vehicles'),
        ('JOBS AND JOBS', 'Jobs and Services'),
    )  
    ESTATE_CHOICES = (
        ('KOMAROCKS', 'Komarocks'),
        ('UMOJA', 'Umoja'),
        ('BURUBURU', 'Buruburu'),
        ('RONGAI', 'Rongai'),
    )
    COUNTY_CHOICES =(
        ('MOMBASA', 'Mombasa'),
        ('NAIROBI', 'Nairobi'),
        ('NAKURU', 'Nakuru'),
        ('KISUMU', 'Kisumu'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
#adding more models here

    location = models.CharField(blank=True, max_length=150)
    county = models.CharField(blank=True, max_length=150, choices=COUNTY_CHOICES)
    estate = models.CharField(blank=True, max_length=150, choices=ESTATE_CHOICES)
    product_type = models.CharField(blank=True, max_length=50, choices=PRODUCT_CHOICES)
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15,unique=True)
    utilities = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)
    Photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    Photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
