# Generated by Django 2.1.5 on 2019-01-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=64)),
                ('website_url', models.CharField(max_length=255)),
                ('website_create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
