# Generated by Django 4.0.2 on 2022-05-05 13:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0009_alter_ovcbireferral_client_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovcbireferral',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccareevents'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='client_category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_service',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_status',
            field=models.CharField(default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_to',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_urgency',
            field=models.CharField(max_length=10),
        ),
    ]
