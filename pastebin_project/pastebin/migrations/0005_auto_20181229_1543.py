# Generated by Django 2.1.4 on 2018-12-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0004_auto_20181229_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]