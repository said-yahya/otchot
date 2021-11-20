# Generated by Django 3.2.8 on 2021-11-20 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zagolovok',
            name='text',
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('zagolovok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.zagolovok')),
            ],
        ),
    ]