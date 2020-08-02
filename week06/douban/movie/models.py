from django.db import models

# Create your models here.
class Movie(models.Model):
    user = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    star = models.FloatField()

    class Meta:
        managed = False
        db_table = 'movie'