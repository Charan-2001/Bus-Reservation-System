# Generated by Django 4.1.7 on 2023-03-03 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus_reservation', '0002_login_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='bus_reservation.bus'),
        ),
    ]