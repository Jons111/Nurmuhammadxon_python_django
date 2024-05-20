# Generated by Django 5.0.4 on 2024-05-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rasm', models.ImageField(upload_to='media')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='team',
            old_name='lavozimi',
            new_name='ishi',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='malumot',
            new_name='text',
        ),
    ]
