# Generated by Django 3.2.3 on 2021-07-17 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_furniture_imageback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='imageBack',
            field=models.ImageField(upload_to='furniture'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='furniture'),
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('nameFurniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.furniture')),
            ],
        ),
    ]