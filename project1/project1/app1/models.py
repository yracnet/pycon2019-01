from django.db import models

# Create your models here.


class Libro(models.Model):
    libro_id = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    autor = models.CharField(max_length=50)
