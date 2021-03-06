# Generated by Django 3.2.7 on 2021-09-23 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0007_auto_20210922_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('mail', models.EmailField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('mail', models.EmailField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Patient_Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this card', primary_key=True, serialize=False)),
                ('disease', models.CharField(max_length=500)),
                ('visit_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Awaiting'), ('c', 'Completed'), ('n', 'Not completed')], default='a', help_text='Visit card', max_length=1)),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.animal')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['visit_date'],
                'permissions': (('can_mark_completed', 'Set visit as completed'),),
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a specie', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='author',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movieinstance',
            name='borrower',
        ),
        migrations.RemoveField(
            model_name='movieinstance',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='MovieInstance',
        ),
        migrations.AddField(
            model_name='animal',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.doctor'),
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.owner'),
        ),
        migrations.AddField(
            model_name='animal',
            name='specie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.specie'),
        ),
    ]
