# Generated by Django 2.2.6 on 2019-10-09 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mreg', '0002_auto_20191002_1227'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sshfp',
            unique_together={('host', 'algorithm', 'hash_type', 'fingerprint')},
        ),
    ]
