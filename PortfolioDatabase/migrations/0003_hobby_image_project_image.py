# Generated by Django 5.1.5 on 2025-02-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0002_alter_hobby_desc_alter_project_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='image',
            field=models.CharField(default='https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png', max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.CharField(default='https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png', max_length=500),
        ),
    ]
