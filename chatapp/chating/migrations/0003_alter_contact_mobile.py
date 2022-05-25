# Generated by Django 3.2.4 on 2022-05-25 12:48

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('chating', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]