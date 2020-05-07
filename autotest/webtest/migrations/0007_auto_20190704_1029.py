# Generated by Django 2.1.4 on 2019-07-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0006_remove_webcasestep_webcasename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcasestep',
            name='webfindmethod',
            field=models.CharField(choices=[('id', 'find_element_by_id'), ('name', 'find_element_by_name'), ('class_name', 'find_element_by_class_name'), ('xpath', 'find_element_by_xpath')], default='id', max_length=200, verbose_name='定位方式'),
        ),
    ]