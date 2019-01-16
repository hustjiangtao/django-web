# Generated by Django 2.1.5 on 2019-01-15 14:59

from django.db import migrations, models
import webview.models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0002_auto_20190112_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('url', models.FileField(storage=webview.models.UpyunStorage(), upload_to='staticfile')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
