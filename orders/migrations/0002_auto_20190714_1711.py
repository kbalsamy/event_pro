# Generated by Django 2.2.1 on 2019-07-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='hall',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='event',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='hall_id',
            field=models.CharField(default='expo', max_length=10),
            preserve_default=False,
        ),
    ]