# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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

