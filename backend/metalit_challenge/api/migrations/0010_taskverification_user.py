# Generated by Django 4.0 on 2022-02-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_challenge_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskverification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
    ]