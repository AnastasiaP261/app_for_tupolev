# Generated by Django 3.2.5 on 2021-07-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenseservers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('host', models.CharField(blank=True, max_length=100, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('creation', models.DateTimeField(blank=True, null=True)),
                ('total_auth', models.IntegerField(blank=True, null=True)),
                ('total_cons', models.IntegerField(blank=True, null=True)),
                ('site', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
                'db_table': 'licenseservers',
                'managed': False,
            },
        ),
    ]
