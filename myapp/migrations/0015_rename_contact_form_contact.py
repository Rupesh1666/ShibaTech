# Generated by Django 5.1 on 2024-08-13 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_contact_form_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact_form',
            new_name='contact',
        ),
    ]
