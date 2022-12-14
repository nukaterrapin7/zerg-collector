# Generated by Django 4.1.2 on 2022-10-29 00:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_amount_essence_absorbtions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mutation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AlterModelOptions(
            name='essence',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='zerg',
            name='mutations',
            field=models.ManyToManyField(to='main_app.mutation'),
        ),
    ]
