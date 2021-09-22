# Generated by Django 3.2.6 on 2021-09-05 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('intransit', 'intransit'), ('canceled', 'canceled'), ('delivered', 'delivered')], default='ordered', max_length=20)),
                ('phone_number', models.PositiveIntegerField(max_length=10)),
                ('delivery_date', models.DateField(null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.mobile')),
            ],
        ),
    ]
