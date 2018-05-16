# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-01 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useradmin', '0002_auto_20170311_1150'),
        ('usershop', '0001_initial'),
        ('authentication', '0005_auto_20170308_2231'),
        ('activities', '0006_auto_20170501_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(choices=[('D', 'Declined'), ('A', 'Accepted'), ('L', 'Low'), ('E', 'Expired')], max_length=1)),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_from', to='authentication.Profile')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useradmin.Medicine')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.Order')),
                ('stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usershop.ShopStock')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_to', to='authentication.Profile')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]