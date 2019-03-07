# Generated by Django 2.1.7 on 2019-03-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190304_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(default=None, max_length=90)),
                ('date', models.DateTimeField(blank=True, default=None)),
                ('featured', models.BooleanField(default=None, null=True)),
            ],
        ),
    ]
