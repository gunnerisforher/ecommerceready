# Generated by Django 4.1.2 on 2022-10-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_remove_cartitem_variation_cartitem_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]