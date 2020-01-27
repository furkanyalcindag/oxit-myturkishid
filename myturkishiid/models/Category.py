from django.db import models


class Category(models.Model):
    key = models.CharField(max_length=256, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s ' % self.key
