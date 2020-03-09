# Generated by Django 2.0 on 2020-03-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键自增')),
                ('name', models.CharField(max_length=12, verbose_name='权限名称')),
            ],
            options={
                'db_table': 'Permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键自增')),
                ('name', models.CharField(max_length=12, verbose_name='角色名称')),
            ],
            options={
                'db_table': 'Role',
            },
        ),
    ]
