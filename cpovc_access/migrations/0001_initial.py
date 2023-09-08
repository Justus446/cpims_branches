# Generated by Django 4.0.2 on 2022-05-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name='HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('get_data', models.TextField(verbose_name='GET Data')),
                ('post_data', models.TextField(verbose_name='POST Data')),
                ('failures_since_start', models.PositiveIntegerField(verbose_name='Failed Logins')),
            ],
            options={
                'db_table': 'auth_login_attempt',
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name='HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'auth_login_accesslog',
            },
        ),
        migrations.CreateModel(
            name='AccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('timestamp_requested', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'auth_login_request',
            },
        ),
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=100, verbose_name='username')),
                ('source_address', models.GenericIPAddressField(db_index=True, verbose_name='source address')),
                ('hostname', models.CharField(max_length=100, verbose_name='hostname')),
                ('successful', models.BooleanField(default=False, verbose_name='successful')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='timestamp')),
                ('user_repr', models.CharField(blank=True, max_length=200, verbose_name='user')),
                ('lockout', models.BooleanField(default=True, help_text='Counts towards lockout count', verbose_name='lockout')),
            ],
            options={
                'verbose_name': 'login attempt',
                'verbose_name_plural': 'login attempts',
                'db_table': 'auth_login_policy',
                'ordering': ('-id',),
                'permissions': (('unlock', 'Unlock by username or IP address'),),
            },
        ),
        migrations.CreateModel(
            name='PasswordChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_repr', models.CharField(max_length=200, verbose_name='user')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('successful', models.BooleanField(default=False, verbose_name='successful')),
                ('is_temporary', models.BooleanField(default=False, verbose_name='is temporary')),
                ('password', models.CharField(default='', editable=False, max_length=128, verbose_name='password')),
            ],
            options={
                'verbose_name': 'password change',
                'verbose_name_plural': 'password changes',
                'db_table': 'auth_password_history',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='UserChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_repr', models.CharField(max_length=200, verbose_name='user')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('by_user_repr', models.CharField(max_length=200, verbose_name='by user')),
            ],
            options={
                'verbose_name': 'user change',
                'verbose_name_plural': 'user changes',
                'db_table': 'auth_user_history',
                'ordering': ('-id',),
            },
        ),
    ]
