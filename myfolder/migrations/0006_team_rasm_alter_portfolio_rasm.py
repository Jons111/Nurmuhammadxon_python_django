# Generated by Django 5.0.4 on 2024-05-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0005_rename_rasm_services_chizma_rename_name_services_ism'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='Rasm',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='rasm',
            field=models.ImageField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]
