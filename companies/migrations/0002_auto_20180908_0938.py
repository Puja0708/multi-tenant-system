# Generated by Django 2.1.1 on 2018-09-08 09:38

from django.db import migrations, models
import multi_tenant_system.utils


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='entry_timestamp',
            field=models.IntegerField(default=multi_tenant_system.utils.get_current_utc_timestamp),
        ),
    ]