# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    tcname = models.CharField(db_column='tcName', max_length=150)  # Field name made lowercase.
    osname = models.CharField(db_column='osName', max_length=200)  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=255)  # Field name made lowercase.
    defgroup = models.CharField(db_column='defGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='lastLogin', blank=True, null=True)  # Field name made lowercase.
    licenseserver = models.CharField(db_column='licenseServer', max_length=100)  # Field name made lowercase.
    licenselevel = models.IntegerField(db_column='licenseLevel', blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(max_length=45)
    deactreason = models.CharField(db_column='deactReason', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Groupmembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    tcname = models.CharField(db_column='tcName', max_length=150)  # Field name made lowercase.
    info = models.CharField(max_length=255, blank=True, null=True)
    group = models.CharField(max_length=255)
    role = models.CharField(max_length=150)
    site = models.CharField(max_length=45)

    class Meta:
        managed = False
        verbose_name = 'Пользователь группы'
        verbose_name_plural = 'Пользователи группы'
        db_table = 'groupmembers'


class Tcgroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parentname = models.CharField(db_column='parentName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    site = models.CharField(max_length=45)
    roles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcgroups'

