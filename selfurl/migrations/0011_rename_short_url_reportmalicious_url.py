# Generated by Django 4.0.3 on 2022-07-03 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfurl', '0010_remove_shortener_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportmalicious',
            old_name='short_url',
            new_name='url',
        ),
    ]
