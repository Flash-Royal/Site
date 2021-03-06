# Generated by Django 3.2.3 on 2021-06-04 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idName', models.CharField(help_text='Enter furniture url id', max_length=100)),
                ('name', models.CharField(help_text='Enter furniture name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='furnitures')),
                ('nameFurniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.furniture')),
            ],
        ),
    ]
