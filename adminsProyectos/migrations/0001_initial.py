# Generated by Django 2.1.3 on 2018-11-07 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=120)),
                ('importancia', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpi', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('proyectos', models.ManyToManyField(through='adminsProyectos.Lista', to='adminsProyectos.Proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='lista',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsProyectos.Proyecto'),
        ),
        migrations.AddField(
            model_name='lista',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsProyectos.Trabajador'),
        ),
    ]