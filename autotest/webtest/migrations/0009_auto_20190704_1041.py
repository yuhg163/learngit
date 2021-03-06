# Generated by Django 2.1.4 on 2019-07-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0008_auto_20190704_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcasestep',
            name='webfindmethod',
            field=models.CharField(choices=[('find_element_by_id', 'id'), ('find_element_by_name', 'name'), ('find_element_by_class_name', 'class_name'), ('find_element_by_xpath', 'xpath')], max_length=200, verbose_name='定位方式'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='weboptmethod',
            field=models.CharField(choices=[('click', 'click'), ('sendkeys', 'sendkeys'), ('check', 'check')], max_length=200, verbose_name='操作方法'),
        ),
    ]
