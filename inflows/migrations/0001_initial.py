# Generated by Django 5.1.4 on 2025-02-16 01:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflows', to='products.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflows', to='suppliers.supplier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inflows', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-created_at'],
            },
        ),
    ]
