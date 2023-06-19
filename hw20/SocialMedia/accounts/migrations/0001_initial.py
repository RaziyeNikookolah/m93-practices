# Generated by Django 4.2.2 on 2023-06-19 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=13)),
                ('national_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addresses', to='accounts.user')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]