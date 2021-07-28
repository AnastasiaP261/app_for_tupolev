# Generated by Django 3.2.5 on 2021-07-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_tcgroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('sd_number', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('action', models.CharField(max_length=50)),
                ('session_id', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.AlterModelOptions(
            name='tcgroups',
            options={'managed': False, 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
    ]