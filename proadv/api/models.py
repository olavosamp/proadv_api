from django.db import models
from django.contrib.postgres.indexes import GinIndex

# Create your models here.
class SearchTerm(models.Model):
    class Meta:
        verbose_name = "termo de pesquisa"
        verbose_name_plural = "termos de pesquisa"
    term = models.fields.CharField(max_length=100)
    classification = models.fields.CharField(max_length=60)

class Publication(models.Model):
    class Meta:
        verbose_name = "publicação"
        verbose_name_plural = "publicações"

        # indexes = [GinIndex(fields=['data'])]

    data = models.JSONField(null=True)
