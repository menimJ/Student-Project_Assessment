# Generated by Django 2.2.6 on 2019-10-23 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assign', to='Project.Project'),
        ),
    ]