from django.db import models

# Create your models here.

class QiPaoShui(models.Model):
    productType = models.CharField(max_length=100)
    productName = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    comment_content = models.TextField(blank=True, null=True)
    comment_time = models.DateField()
    sentiments = models.FloatField()
    
    class Meta:
        managed = False
        db_table = 'product'
