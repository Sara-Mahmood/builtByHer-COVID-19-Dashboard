# Generated by Django 2.2.7 on 2020-04-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily_cases',
            options={'verbose_name': 'Daily Cases', 'verbose_name_plural': 'Daily Cases'},
        ),
        migrations.AlterField(
            model_name='daily_cases',
            name='province',
            field=models.CharField(choices=[('SINDH', 'Sindh'), ('PUNJAB', 'Punjab'), ('KPK', 'KPK'), ('KPTD', 'KPTD'), ('GB', 'GB'), ('AJK', 'AJK'), ('ICT', 'ICT'), ('TAFTAN_MOBILE_LAB', 'Taftan_mobile_lab'), ('BALOCHISTAN', 'Balochistan')], max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='daily_cases',
            unique_together={('date', 'province')},
        ),
        migrations.RemoveField(
            model_name='daily_cases',
            name='total_tested_negative',
        ),
    ]
