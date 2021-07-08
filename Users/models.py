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