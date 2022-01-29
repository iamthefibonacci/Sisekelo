# Generated by Django 4.0 on 2022-01-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_rename_course_slug_accredited_program_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='accredited_program',
            name='career_prospects',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accredited_program',
            name='payment_type',
            field=models.CharField(choices=[('EFT', 'EFT'), ('CARDS', 'CARDS'), ('TRANSFER', 'TRANSFER')], default='EFT', max_length=50),
        ),
        migrations.AddField(
            model_name='accredited_program',
            name='target_audience',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
