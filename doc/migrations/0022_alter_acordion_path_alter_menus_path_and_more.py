# Generated by Django 4.0.3 on 2022-06-04 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0021_alter_acordion_path_alter_menus_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acordion',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('selfurl:django.contrib.sitemaps.views.sitemap', 'Django.contrib.sitemaps.views.sitemap'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:password_reset', 'Password_reset'), ('accounts:password_reset_done', 'Password_reset_done'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
        migrations.AlterField(
            model_name='menus',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('selfurl:django.contrib.sitemaps.views.sitemap', 'Django.contrib.sitemaps.views.sitemap'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:password_reset', 'Password_reset'), ('accounts:password_reset_done', 'Password_reset_done'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
        migrations.AlterField(
            model_name='metatext',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('selfurl:django.contrib.sitemaps.views.sitemap', 'Django.contrib.sitemaps.views.sitemap'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:password_reset', 'Password_reset'), ('accounts:password_reset_done', 'Password_reset_done'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
    ]