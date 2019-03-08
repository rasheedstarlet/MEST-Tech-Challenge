from django.db import models

from django.urls import reverse

# Create your models here.
class House(models.Model):
    CATEGORY_CHOICES = (
    ('For Rent', 'FOR RENT'),
    ('For Sale', 'FOR SALE'),
    )

    seller      = models.CharField(max_length=50)
    title        = models.CharField(max_length=100)
    picture     = models.ImageField(upload_to='houses/%Y/%m/%d/', default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    price       = models.IntegerField(default=None, null=True, blank=True)
    address     = models.CharField(max_length=50, default=None, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    category    = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='All')
    lease_options = models.CharField(max_length=250)
    garage       = models.IntegerField()
    furnished    = models.CharField(max_length=20)
    reference    = models.IntegerField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.description

    def amount(self):
        return "GH₵"+ str(self.price)
'''
    def get_absolute_url(self):
        return reverse('home:home', args = [str(self.pk)])
'''
