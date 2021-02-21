# Generated by Django 3.1.5 on 2021-02-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
