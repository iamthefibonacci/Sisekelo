# Generated by Django 4.0 on 2022-01-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.CharField(default='EF70C5', max_length=32, null=True),
        ),
    ]
