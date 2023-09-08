# Generated by Django 4.0.4 on 2022-05-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0002_alter_ovcsibling_id_alter_regbiometric_id_and_more'),
        ('cpovc_forms', '0010_ovcbireferral_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovcbireferral',
            name='client_category',
            field=models.CharField(default='Caregiver', max_length=20),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='person',
            field=models.ForeignKey(default=60, on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson'),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='ref_caregiver',
            field=models.ForeignKey(default=59, on_delete=django.db.models.deletion.CASCADE, related_name='refferal_caregiver', to='cpovc_registry.regperson'),
        ),
        migrations.AlterField(
            model_name='ovcbireferral',
            name='refferal_urgency',
            field=models.CharField(default='OVC', max_length=10),
        ),
    ]
