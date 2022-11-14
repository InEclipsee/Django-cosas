# Generated by Django 4.1.3 on 2022-11-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('dueno', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRecepcion', models.DateField()),
                ('conserje', models.CharField(max_length=50)),
                ('remitente', models.CharField(max_length=50)),
                ('destinatario', models.CharField(max_length=50)),
                ('idResidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.residencia')),
            ],
        ),
    ]