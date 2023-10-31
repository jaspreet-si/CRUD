from django.db import models

# Create your models here.
class waiter(models.Model):
    name=models.CharField(max_length=150)
    age=models.PositiveIntegerField()
    Phone=models.CharField(max_length=10)
    Email=models.EmailField(blank=False)
    Address=models.CharField(max_length=300)

    def __str__ (self):
        return self.Name