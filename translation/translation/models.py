from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Product Name'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.name
