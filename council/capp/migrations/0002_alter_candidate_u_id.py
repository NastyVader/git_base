# Generated by Django 3.2.5 on 2021-12-23 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='U_ID',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='capp.union'),
        ),
    ]