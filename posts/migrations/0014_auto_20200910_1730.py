# Generated by Django 2.2.6 on 2020-09-10 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20200909_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='posts.Post', verbose_name='Пост этого комментария'),
        ),
    ]
