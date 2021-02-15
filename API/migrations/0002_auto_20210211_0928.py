# Generated by Django 3.1.6 on 2021-02-11 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='ate_uploaded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='attachment',
            field=models.FileField(default=None, null=True, upload_to='attachment/'),
        ),
        migrations.AddField(
            model_name='document',
            name='barcode',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.category'),
        ),
        migrations.AddField(
            model_name='document',
            name='date_completed',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='document',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='document_no',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.BooleanField(default=None),
        ),
    ]