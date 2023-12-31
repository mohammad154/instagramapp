# Generated by Django 4.2.3 on 2023-07-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.IntegerField()),
                ('comment', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('type', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=150, null=True)),
                ('video', models.FileField(null=True, upload_to='videos/%y')),
                ('image', models.ImageField(null=True, upload_to='images/%y')),
                ('text', models.TextField(max_length=1500, null=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
