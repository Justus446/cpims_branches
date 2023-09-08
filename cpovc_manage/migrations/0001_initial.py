# Generated by Django 4.0.2 on 2022-05-01 15:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpovc_registry', '0001_initial'),
        ('cpovc_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NOTTTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=150)),
                ('travel_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('no_applied', models.IntegerField(default=0)),
                ('no_cleared', models.IntegerField(default=0)),
                ('no_returned', models.IntegerField(blank=True, default=0, null=True)),
                ('contacts', models.CharField(blank=True, max_length=150, null=True)),
                ('reason', models.CharField(max_length=150)),
                ('sponsor', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True, null=True)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(default=0)),
                ('is_void', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Non Objection to Travel - Travel',
                'verbose_name_plural': 'Non Objection to Travel - Travels',
                'db_table': 'nott_travel',
            },
        ),
        migrations.CreateModel(
            name='NOTTChild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned', models.BooleanField(default=False)),
                ('cleared', models.BooleanField(default=False)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_manage.notttravel')),
            ],
            options={
                'verbose_name': 'Non Objection to Travel - Child',
                'verbose_name_plural': 'Non Objection to Travel - Children',
                'db_table': 'nott_child',
            },
        ),
        migrations.CreateModel(
            name='NOTTChaperon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_void', models.BooleanField(default=False)),
                ('other_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccasepersons')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_manage.notttravel')),
            ],
            options={
                'verbose_name': 'Non Objection to Travel - Chaperon',
                'verbose_name_plural': 'Non Objection to Travel - Chaperons',
                'db_table': 'nott_chaperon',
            },
        ),
    ]
