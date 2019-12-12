# Generated by Django 2.2.8 on 2019-12-12 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0004_2_1'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_intent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.PaymentIntent'),
        ),
    ]
