# Generated by Django 2.0.5 on 2018-05-20 06:01

from django.conf import settings
from django.db import migrations, models
import nomadgram.images.models
import nomadgram.users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0002_auto_20180513_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=nomadgram.users.models.User, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=nomadgram.users.models.User, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(null=True, on_delete=nomadgram.images.models.Image, to='images.Image'),
        ),
        migrations.AddField(
            model_name='image',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=nomadgram.users.models.User, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='image',
            field=models.ForeignKey(null=True, on_delete=nomadgram.images.models.Image, to='images.Image'),
        ),
    ]
