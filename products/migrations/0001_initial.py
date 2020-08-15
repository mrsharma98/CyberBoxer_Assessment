# Generated by Django 3.1 on 2020-08-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20200815_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofileinfo')),
            ],
        ),
    ]