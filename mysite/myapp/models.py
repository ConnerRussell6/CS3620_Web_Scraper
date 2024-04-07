from django.db import models

# Create your models here.


class Link(models.Model):

    address = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name if self.name else f"Link-{self.id}"


