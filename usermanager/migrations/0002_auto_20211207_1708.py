# Generated by Django 3.2.9 on 2021-12-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='doc_id',
        ),
        migrations.AddField(
            model_name='history',
            name='bot_id',
            field=models.IntegerField(default=0, verbose_name='bot_id'),
        ),
        migrations.AlterField(
            model_name='history',
            name='answer',
            field=models.CharField(max_length=256, verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='history',
            name='query',
            field=models.CharField(max_length=256, verbose_name='query'),
        ),
    ]