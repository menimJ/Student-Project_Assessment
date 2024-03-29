# Generated by Django 2.2.6 on 2019-10-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('can_view_project', 'Can View Project'), ('can_grade_project', 'Can grade Project '))},
        ),
        migrations.AlterField(
            model_name='project',
            name='abstract',
            field=models.TextField(help_text=' Student Project Abstract'),
        ),
        migrations.AlterField(
            model_name='project',
            name='analysis',
            field=models.TextField(help_text='Student Project Analysis'),
        ),
        migrations.AlterField(
            model_name='project',
            name='conclusion',
            field=models.TextField(help_text='Student Project Conclusion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='literature',
            field=models.TextField(help_text='Student Project Literature'),
        ),
        migrations.AlterField(
            model_name='project',
            name='method',
            field=models.TextField(help_text='Student Project Method'),
        ),
    ]
