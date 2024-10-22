# Generated by Django 5.1.1 on 2024-10-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='blogs/')),
            ],
        ),
    ]
