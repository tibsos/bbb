# Generated by Django 4.1.4 on 2023-02-27 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('initials', models.CharField(max_length=3)),
                ('premium', models.BooleanField(default=False)),
                ('premium_since', models.DateTimeField(blank=True, null=True)),
                ('premium_invite_uid', models.CharField(max_length=7)),
                ('premium_friend_offer_shown', models.BooleanField(default=False)),
                ('dark_mode', models.BooleanField(default=False)),
                ('password_recovery_token', models.TextField(blank=True, null=True)),
                ('invited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.profile')),
                ('invited_friends', models.ManyToManyField(blank=True, related_name='friends_invited', to='user.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]
