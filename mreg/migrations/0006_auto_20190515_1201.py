# Generated by Django 2.2.1 on 2019-05-15 10:01

from django.db import migrations, models
import mreg.fields
import mreg.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mreg', '0005_hostgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cname',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='forwardzone',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='forwardzone',
            name='primary_ns',
            field=mreg.fields.DnsNameField(max_length=253, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='forwardzonedelegation',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='hostgroup',
            name='name',
            field=mreg.fields.LCICharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='mx',
            name='mx',
            field=mreg.fields.DnsNameField(max_length=253, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='nameserver',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='naptr',
            name='regex',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='naptr',
            name='replacement',
            field=mreg.fields.LCICharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='naptr',
            name='service',
            field=mreg.fields.LCICharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='reversezone',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_reverse_zone_name]),
        ),
        migrations.AlterField(
            model_name='reversezone',
            name='primary_ns',
            field=mreg.fields.DnsNameField(max_length=253, validators=[mreg.validators.validate_hostname]),
        ),
        migrations.AlterField(
            model_name='reversezonedelegation',
            name='name',
            field=mreg.fields.DnsNameField(max_length=253, unique=True, validators=[mreg.validators.validate_reverse_zone_name]),
        ),
        migrations.AlterField(
            model_name='srv',
            name='name',
            field=mreg.fields.LCICharField(max_length=255, validators=[mreg.validators.validate_srv_service_text]),
        ),
        migrations.AlterField(
            model_name='srv',
            name='target',
            field=mreg.fields.DnsNameField(max_length=253, validators=[mreg.validators.validate_hostname]),
        ),
    ]
