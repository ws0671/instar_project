# Generated by Django 3.2.4 on 2021-06-17 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('social', '0009_auto_20210610_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(blank=True, null=True, related_name='following', to='member.Member')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='member.member')),
            ],
        ),
    ]
