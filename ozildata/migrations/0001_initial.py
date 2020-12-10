# Generated by Django 3.1.4 on 2020-12-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZilData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dersbaslangicsaati', models.TimeField(default='09:00', verbose_name='Derslerin Başlangıç Saati')),
                ('toplanmasuresi', models.TimeField(default='00:10', verbose_name='Toplanma Süresi')),
                ('ogretmenzilsuresi', models.TimeField(default='00:03', verbose_name='Öğretmen Ders Bildirim Zili')),
                ('derssayisi', models.SmallIntegerField(default=10, verbose_name='Günlük Ders Sayısı')),
                ('derssuresi', models.TimeField(default='00:40', verbose_name='Ders Süresi')),
                ('tenefussuresi', models.TimeField(default='00:10', verbose_name='Tenefüs Süresi')),
                ('oglenarasiders', models.SmallIntegerField(default=6, verbose_name='Öğlen Arası')),
                ('oglenarasisuresi', models.TimeField(default='00:45', verbose_name='Öğlen Arası Süresi')),
                ('zilgun', models.SlugField(default=0, verbose_name='Gün No')),
                ('xzilgun', models.SmallIntegerField(choices=[[0, 'Pazartesi'], [1, 'Salı'], [2, 'Çarşamba'], [3, 'Perşembe'], [4, 'Cuma'], [5, 'Cumartesi'], [6, 'Pazar']], default=0, unique=True, verbose_name='Tanımlanan Günü')),
                ('active', models.BooleanField(default=False, verbose_name='Aktif Pasif')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'db_table': 'zildefault',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ZilMelodi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melodiad', models.TextField(verbose_name='Melodi Adı')),
                ('yol', models.TextField(verbose_name='Path')),
            ],
            options={
                'db_table': 'melodipath',
                'managed': True,
            },
        ),
    ]