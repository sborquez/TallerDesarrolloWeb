# Generated by Django 2.0.5 on 2018-07-05 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('contenido', models.TextField()),
                ('publicacion', models.TimeField(auto_now_add=True)),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogger', to='blog.Blogger')),
            ],
            options={
                'ordering': ['publicacion'],
            },
        ),
    ]
