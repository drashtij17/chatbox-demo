# Generated by Django 3.2.4 on 2022-05-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chating', '0003_alter_contact_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_read',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
