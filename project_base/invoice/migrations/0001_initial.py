# Generated by Django 2.2.4 on 2019-08-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='updated at')),
                ('amount_of_quantities', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Amount of quantities')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cost')),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending')], default='pending', max_length=30, verbose_name='status')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
