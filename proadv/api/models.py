from django.db import models
from django.contrib.postgres.indexes import GinIndex

# Create your models here.
class SearchTerm(models.Model):
    class Meta:
        verbose_name = "termo de pesquisa"
        verbose_name_plural = "termos de pesquisa"

    classification = models.fields.CharField(max_length=60, verbose_name="classificação")
    term = models.fields.CharField(max_length=100, verbose_name="termo de pesquisa")

class Publication(models.Model):
    class Meta:
        verbose_name = "publicação"
        verbose_name_plural = "publicações"

    types = models.ManyToManyField(SearchTerm, related_name="publications")
    date = models.DateTimeField(null=True, verbose_name="data")
    content = models.TextField(null=True, verbose_name="conteúdo")
    observation = models.TextField(null=True, verbose_name="observação")
    code = models.IntegerField(null=True, verbose_name="código do diário")
