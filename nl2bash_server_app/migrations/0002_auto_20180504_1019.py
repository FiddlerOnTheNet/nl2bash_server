# Generated by Django 2.0.4 on 2018-05-04 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nl2bash_server_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BashCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmd', models.TextField(help_text='A bash command.', max_length=300, null=True, verbose_name='Bash Command')),
            ],
        ),
        migrations.CreateModel(
            name='EnglishDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmd', models.TextField(help_text='A natural language description of a bash command.', max_length=300, null=True, verbose_name='Natural Language Command')),
                ('num_verified', models.IntegerField(default=0, verbose_name='Number of verified command pairs')),
            ],
        ),
        migrations.RemoveField(
            model_name='commandpairinstance',
            name='cmd_pair',
        ),
        migrations.AlterField(
            model_name='commandpair',
            name='bash',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nl2bash_server_app.BashCommand'),
        ),
        migrations.AlterField(
            model_name='commandpair',
            name='nl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nl2bash_server_app.EnglishDescription'),
        ),
        migrations.DeleteModel(
            name='CommandPairInstance',
        ),
    ]
