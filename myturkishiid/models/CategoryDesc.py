from django.db import models



class CategoryDesc(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    lang = models.ForeignKey('Language', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='İlan Kategorisi')

    def __str__(self):
        return '%s ' % self.name
