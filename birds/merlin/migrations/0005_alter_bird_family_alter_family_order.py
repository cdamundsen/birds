# Generated by Django 5.1.7 on 2025-03-25 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0004_family_order_bird_family_family_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='birds', to='merlin.family'),
        ),
        migrations.AlterField(
            model_name='family',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='families', to='merlin.order'),
        ),
    ]
