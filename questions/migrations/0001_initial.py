# Generated by Django 4.0.1 on 2022-02-06 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categ_name', models.CharField(max_length=100)),
                ('main_title', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.TextField()),
                ('question_body', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.title')),
            ],
        ),
    ]
