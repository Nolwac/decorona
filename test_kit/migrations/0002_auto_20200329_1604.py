# Generated by Django 2.1.2 on 2020-03-29 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_kit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algorithm',
            name='initial_decision_box',
        ),
        migrations.RemoveField(
            model_name='connector',
            name='connect_from',
        ),
        migrations.RemoveField(
            model_name='connector',
            name='operation',
        ),
        migrations.AddField(
            model_name='connector',
            name='connected_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_kit.DecisionBox'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='decisionbox',
            name='algorthm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_kit.Algorithm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='connector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_kit.Connector'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='decisionbox',
            name='threshold',
            field=models.IntegerField(default=1),
        ),
    ]
