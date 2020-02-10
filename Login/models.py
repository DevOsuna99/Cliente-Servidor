from django.db import models
from django.util import timezone

class Exmaple2(models.Model):
    name = models.CharField(max_length=254, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class meta:
        db_table = 'Example2'

# Create your models here.
