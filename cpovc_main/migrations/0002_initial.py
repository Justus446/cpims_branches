# Generated by Django 4.0.2 on 2022-04-25 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpovc_registry', '0001_initial'),
        ('cpovc_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coreservices',
            name='beneficiary_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_beneficiary', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='coreservices',
            name='workforce_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_workforce', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='coreencountersnotes',
            name='beneficiary_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encounter_n_beneficiary', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='coreencountersnotes',
            name='encounter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.coreencounters'),
        ),
        migrations.AddField(
            model_name='coreencountersnotes',
            name='workforce_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encounter_n_workforce', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='coreencounters',
            name='beneficiary_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encounter_beneficiary', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='coreencounters',
            name='workforce_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encounter_workforce', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='coreadverseconditions',
            name='beneficiary_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverse_beneficiary', to='cpovc_registry.regperson'),
        ),
        migrations.AddField(
            model_name='adminuploadforms',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.forms'),
        ),
        migrations.AddField(
            model_name='adminpreferences',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson'),
        ),
        migrations.AlterUniqueTogether(
            name='reportssetsorgunits',
            unique_together={('set', 'org_unit_id')},
        ),
    ]