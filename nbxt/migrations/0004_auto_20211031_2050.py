# Generated by Django 3.2.7 on 2021-10-31 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbxt', '0003_auto_20211031_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='jj1001',
            name='c34',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='jj1001',
            name='c35',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='jj1001',
            name='c01',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jj1001',
            name='c02',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jj1001',
            name='c03',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='jj1001',
            name='c04',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
