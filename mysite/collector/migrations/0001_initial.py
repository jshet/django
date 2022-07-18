# Generated by Django 4.0.6 on 2022-07-17 02:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('curatorial_statement', models.TextField()),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('figure', models.ImageField(upload_to='')),
                ('collected_from', models.CharField(max_length=500)),
                ('desciption', models.TextField()),
                ('collected_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fragment_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.work')),
                ('variant_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant_of_work', to='collector.work')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_opened', models.DateTimeField(default=datetime.datetime.now)),
                ('date_closed', models.DateTimeField(default=datetime.datetime.now)),
                ('curatorial_statement', models.TextField()),
                ('contributors', models.ManyToManyField(related_name='contributors', to=settings.AUTH_USER_MODEL)),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exhibits', models.ManyToManyField(to='collector.exhibit')),
                ('guest_list', models.ManyToManyField(related_name='guests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exhibit',
            name='works',
            field=models.ManyToManyField(to='collector.work'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('reactions', models.IntegerField(default=0)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.work')),
            ],
        ),
    ]
