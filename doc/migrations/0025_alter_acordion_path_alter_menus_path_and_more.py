# Generated by Django 4.0.3 on 2022-08-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0024_exsite_site_meta_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acordion',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('selfurl:django.contrib.sitemaps.views.sitemap', 'Django.contrib.sitemaps.views.sitemap'), ('selfurl:robot', 'Robot'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:password_reset', 'Password_reset'), ('accounts:password_reset_done', 'Password_reset_done'), ('accounts:password_reset_complete', 'Password_reset_complete'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
        migrations.AlterField(
            model_name='menus',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('selfurl:django.contrib.sitemaps.views.sitemap', 'Django.contrib.sitemaps.views.sitemap'), ('selfurl:robot', 'Robot'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:password_reset', 'Password_reset'), ('accounts:password_reset_done', 'Password_reset_done'), ('accounts:password_reset_complete', 'Password_reset_complete'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
        migrations.AlterField(
            model_name='metatext',
            name='path',
            field=models.CharField(choices=[('selfurl:index', 'Index'), ('selfurl:report_malicious', 'Report_malicious'), ('selfurl:statistics', 'Statistics'), ('selfurl:django.contrib.sitemaps.views.sitemap', 'Django.contrib.sitemaps.views.sitemap'), ('selfurl:robot', 'Robot'), ('contact:contact', 'Contact'), ('doc:webmanifest', 'Webmanifest'), ('doc:terms_and_conditions', 'Terms_and_conditions'), ('doc:privacy_policy', 'Privacy_policy'), ('accounts:signup', 'Signup'), ('accounts:login', 'Login'), ('accounts:password_reset', 'Password_reset'), ('accounts:password_reset_done', 'Password_reset_done'), ('accounts:password_reset_complete', 'Password_reset_complete'), ('accounts:change_pass', 'Change_pass')], max_length=50),
        ),
    ]
