# Generated by Django 3.1.6 on 2021-02-11 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20210211_0940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-id']},
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('id', 'document_no')},
        ),
    ]
