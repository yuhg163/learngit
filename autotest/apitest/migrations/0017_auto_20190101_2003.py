# Generated by Django 2.1.4 on 2019-01-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0016_auto_20180129_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apistep',
            name='apiresponse',
            field=models.CharField(max_length=10000, null=True, verbose_name='响应数据'),
        ),
    ]
