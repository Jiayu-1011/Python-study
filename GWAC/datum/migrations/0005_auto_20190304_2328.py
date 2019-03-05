# Generated by Django 2.1.5 on 2019-03-04 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0004_auto_20190304_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='action_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='useraction',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]