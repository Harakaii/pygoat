# Generated by Django 4.0.4 on 2022-08-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0020_af_session_id_alter_af_admin_lockout_cooldown'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSRF_user_tbl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('balance', models.IntegerField(default=0)),
                ('is_loggedin', models.BooleanField(default=False)),
            ],
        ),
    ]