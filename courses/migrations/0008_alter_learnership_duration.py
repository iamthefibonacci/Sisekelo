# Generated by Django 4.0 on 2022-01-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_accredited_program_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnership',
            name='duration',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
