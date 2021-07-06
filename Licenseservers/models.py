from django.db import models


class Licenseservers(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    creation = models.DateTimeField(blank=True, null=True)
    total_auth = models.IntegerField(blank=True, null=True)
    total_cons = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'
        managed = False
        db_table = 'licenseservers'