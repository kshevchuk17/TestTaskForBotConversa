# Generated by Django 3.2.3 on 2021-05-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0010_alter_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(auto_now_add=True, verbose_name='Due date'),
        ),
    ]