# Generated by Django 5.0.6 on 2024-05-29 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoredRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=255, verbose_name='Request')),
                ('text', models.CharField(max_length=255, verbose_name='Text')),
            ],
        ),
    ]