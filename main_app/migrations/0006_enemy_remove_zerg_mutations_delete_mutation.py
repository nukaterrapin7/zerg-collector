# Generated by Django 4.1.2 on 2022-10-29 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_mutation_alter_essence_options_zerg_mutations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(choices=[('T', 'Terran'), ('P', 'Protoss'), ('Z', 'Zerg')], default='T', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='zerg',
            name='mutations',
        ),
        migrations.DeleteModel(
            name='Mutation',
        ),
    ]