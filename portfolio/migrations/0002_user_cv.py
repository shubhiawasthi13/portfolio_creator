# Generated by Django 5.1.4 on 2024-12-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cv',
            field=models.FileField(default=2, upload_to='portfolio/uploads/'),
            preserve_default=False,
        ),
    ]
