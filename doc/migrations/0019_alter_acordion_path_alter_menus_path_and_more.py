# Generated by Django 4.0.3 on 2022-04-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0018_acordion_fa_icon_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acordion',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
        migrations.AlterField(
            model_name='menus',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
        migrations.AlterField(
            model_name='metatext',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
    ]
