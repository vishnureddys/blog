# Generated by Django 3.2.7 on 2021-09-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.TextField(default='Make sure you check out this post!!'),
            preserve_default=False,
        ),
    ]