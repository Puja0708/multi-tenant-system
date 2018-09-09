# Generated by Django 2.1.1 on 2018-09-09 21:30

from django.db import migrations, models
import django.db.models.deletion
import multi_tenant_system.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('first_name', models.CharField(max_length=14, unique=True)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('hire_date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('display_id', models.CharField(max_length=5, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.BigIntegerField()),
                ('entry_timestamp', models.IntegerField(default=multi_tenant_system.utils.get_current_utc_timestamp)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmployeeRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=5)),
                ('entry_timestamp', models.IntegerField(default=multi_tenant_system.utils.get_current_utc_timestamp)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.EmployeeRoles'),
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='teams.Teams'),
        ),
    ]
