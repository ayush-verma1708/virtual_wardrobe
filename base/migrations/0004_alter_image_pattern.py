# Generated by Django 4.2.2 on 2024-02-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_image_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pattern',
            field=models.CharField(choices=[('Horizontal Stripes', 'Horizontal Stripes'), ('Vertical Stripes', 'Vertical Stripes'), ('Checkered', 'Checkered'), ('Graphic Print', 'Graphic Print'), ('Plain', 'Plain')], max_length=255),
        ),
    ]
