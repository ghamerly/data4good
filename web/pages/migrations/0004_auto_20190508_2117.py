# Generated by Django 2.2 on 2019-05-09 02:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_site_program_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='ce',
            name='childnutdir_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='childnutdir_first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='childnutdir_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='childnutdir_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='childnutdir_salutation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='childnutdir_title_position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ce',
            name='most_current_record',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='superintendent_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='superintendent_first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='superintendent_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='superintendent_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='superintendent_salutation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ce',
            name='superintendent_title_position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='primary_auth_rep_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='primary_auth_rep_first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='primary_auth_rep_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='primary_auth_rep_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='primary_auth_rep_salutation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='primary_auth_rep_title_position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_supervisor_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_supervisor_first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_supervisor_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_supervisor_phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_supervisor_salutation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='site_supervisor_title_position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ce',
            name='county_district_code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='ce',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='ce',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='ce',
            name='mailing_address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ce',
            name='street_address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='ce_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.CE'),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mailing_address1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mailing_address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mailing_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mailing_state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mailing_zip',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='program_contact_salutation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='program_contact_title_position',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='rural_or_urban_code',
            field=models.CharField(blank=True, choices=[('RURAL', 'Rural'), ('URBAN', 'Urban')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='sfsp_site_type',
            field=models.CharField(blank=True, choices=[('CAMP_NON_RES', 'Camp-Non-Residential'), ('CAMP_RES', 'Camp-Residential'), ('CLOSED_ENROLLED_NEEDY', 'Closed-Enrolled in Needy Area'), ('CLOSED_ENROLLED_NON_NEEDY', 'Closed-Enrolled in Non-Needy Area'), ('HOMELESS', 'Homeless'), ('OPEN', 'Open'), ('ROPEN', 'Restricted Open'), ('OTHER', 'Other')], default='OTHER', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='sso_site_type',
            field=models.CharField(blank=True, choices=[('CAMP', 'Camp'), ('CLOSED', 'Closed'), ('OPEN', 'Open'), ('ROPEN', 'Open Restricted'), ('OTHER', 'Other')], default='OTHER', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='street_address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='type_of_sfsp_org',
            field=models.CharField(blank=True, choices=[('NSC', 'Nonresidential Summer Camp'), ('PNP', 'Private Non Profit'), ('RC', 'Residential Camp'), ('SFA', 'School Food Authority'), ('UG', 'Unit of Government'), ('OTHER', 'Other')], default='OTHER', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='type_of_snp_org',
            field=models.CharField(blank=True, choices=[('CHARTER', 'Charter'), ('PRIVATE', 'Private'), ('PUBLIC', 'Public'), ('RCCI', 'Residential Child Care Institution'), ('OTHER', 'Other')], default='OTHER', max_length=100, null=True),
        ),
    ]
