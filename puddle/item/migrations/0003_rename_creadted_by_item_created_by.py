# Generated by Django 4.1.6 on 2023-02-08 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='creadted_by',
            new_name='created_by',
        ),
    ]
