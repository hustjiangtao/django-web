# Generated by Django 2.1.5 on 2019-01-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='website',
            name='website_category',
            field=models.SmallIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='website',
            name='website_desc',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='website',
            name='website_logo',
            field=models.URLField(default='https://www.gravatar.com/avatar/86002c942ce536ce28e806d42edcdfef?s=40', max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='website_url',
            field=models.URLField(max_length=255),
        ),
    ]
