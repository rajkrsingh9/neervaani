# Generated by Django 4.2 on 2024-12-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neervaani_app', '0003_alter_cropcalculator_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('green_water_footprint', models.FloatField()),
                ('blue_water_footprint', models.FloatField()),
                ('grey_water_footprint', models.FloatField()),
                ('total_water_footprint', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]