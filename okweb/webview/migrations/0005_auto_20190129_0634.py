# Generated by Django 2.1.5 on 2019-01-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0004_auto_20190116_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='website_logo',
            field=models.URLField(max_length=255),
        ),
    ]