# Generated by Django 4.2.3 on 2023-08-30 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Handbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('factoryNumberOfMachine', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Зав. № машины')),
                ('factoryNumberOfEngine', models.CharField(max_length=128, verbose_name='Зав. № двигателя')),
                ('factoryNumberOfTransmission', models.CharField(max_length=128, verbose_name='Зав. № трансмиссии')),
                ('factoryNumberOfMainAxle', models.CharField(max_length=128, verbose_name='Зав. № ведущего моста')),
                ('factoryNumberOfSteeringAxle', models.CharField(max_length=128, verbose_name='Зав. № управляемого моста')),
                ('supplyContract', models.CharField(max_length=128, verbose_name='Договор поставки №, дата')),
                ('dateOfShipment', models.DateField(verbose_name='Дата отгрузки с завода')),
                ('consumer', models.CharField(max_length=128, verbose_name='Грузополучатель')),
                ('operationAddress', models.CharField(max_length=128, verbose_name='Адрес поставки')),
                ('additionalOptions', models.TextField(verbose_name='Доп. опции')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_client', to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('modelOfEngine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_modelOfEngine', to='Handbook.modelofengine', verbose_name='Модель двигателя')),
                ('modelOfMachine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_modelOfMachine', to='Handbook.modelofmachine', verbose_name='Модель техники')),
                ('modelOfMainAxle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_modelofMainAxle', to='Handbook.modelofmainaxle', verbose_name='Модель ведущего моста')),
                ('modelOfSteeringAxle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_modelOfSteeringAxle', to='Handbook.modelofsteeringaxle', verbose_name='Модель управляемого моста')),
                ('modelOfTransmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_modelOfTransmission', to='Handbook.modeloftransmission', verbose_name='Модель трансмиссии')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machine_serviceCompany', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ['-dateOfShipment'],
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfMaintenance', models.DateField(verbose_name='Дата проведения ТО')),
                ('operatingTime', models.IntegerField(verbose_name='Наработка, м/час')),
                ('numberOrderWork', models.CharField(max_length=128, verbose_name='№ заказ-наряда')),
                ('dateOrderWork', models.DateField(verbose_name='Дата заказ-наряда')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='MainApp.machine', verbose_name='Машина')),
                ('maintenanceServiceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_servicecompany', to=settings.AUTH_USER_MODEL, verbose_name='Организация, проводившая ТО')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_serviceCompany', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания')),
                ('typeOfMaintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_typeofmaintenance', to='Handbook.typeofmaintenance', verbose_name='Вид ТО')),
            ],
            options={
                'verbose_name': 'Техническое Обслуживание',
                'verbose_name_plural': 'Техническое Обслуживание',
                'ordering': ['-dateOfMaintenance'],
            },
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfFailure', models.DateField(verbose_name='Дата отказа')),
                ('operatingTime', models.IntegerField(verbose_name='Наработка, м/час')),
                ('descriptionOfFailure', models.CharField(max_length=128, verbose_name='Описание отказа')),
                ('usedSpareParts', models.CharField(blank=True, max_length=128, verbose_name='Используемые запасные части')),
                ('dateOfRecovery', models.DateField(verbose_name='Дата восстановления')),
                ('downtimeOfMachine', models.IntegerField(blank=True, verbose_name='Время простоя')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_machine', to='MainApp.machine', verbose_name='Машина')),
                ('nodeOfFailure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_nodeoffailure', to='Handbook.typeoffailure', verbose_name='Узел отказа')),
                ('recoveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handbook_recoverymethod', to='Handbook.methodofrecovery', verbose_name='Способ восстановления')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_serviceCompany', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
                'ordering': ['-dateOfFailure'],
            },
        ),
    ]
