from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    createdAt = models.DateField(auto_now_add = True)
    price = models.IntegerField()


    def __str_(self):
        self.title
