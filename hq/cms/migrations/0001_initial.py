# Generated by Django 4.0.5 on 2022-06-23 05:22

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=200)),
                ('access_role', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cwf',
            fields=[
                ('cwf_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('excel_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, upload_to='exhibits/')),
                ('alt_text', models.CharField(blank=True, max_length=100)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('exhibit_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='exhibits/')),
                ('alt_text', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Kt',
            fields=[
                ('kt_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('cwf', models.ManyToManyField(to='cms.cwf')),
            ],
        ),
        migrations.CreateModel(
            name='Qtype',
            fields=[
                ('qtype_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_code', models.CharField(max_length=20, unique=True)),
                ('role_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('stage_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('role', models.ManyToManyField(to='cms.role')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('context', models.JSONField(blank=True, null=True)),
                ('text', models.CharField(max_length=100)),
                ('options', models.JSONField(blank=True, null=True)),
                ('score_type', models.CharField(max_length=10)),
                ('score_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('resources', models.JSONField(blank=True, null=True)),
                ('last_edited', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('idealtime', models.FloatField(blank=True, null=True)),
                ('difficulty_level', models.CharField(blank=True, max_length=50, null=True)),
                ('misc', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[('SAVED', 'Saved'), ('UNDERREVIEW', 'Under Review'), ('REVIEWED', 'Reviewed'), ('ARCHIVED', 'Archived')], default='SAVED', max_length=20)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_approver', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_creator', to=settings.AUTH_USER_MODEL)),
                ('cwf', models.ManyToManyField(blank=True, to='cms.cwf')),
                ('excels', models.ManyToManyField(blank=True, to='cms.excel')),
                ('exhibits', models.ManyToManyField(blank=True, to='cms.exhibit')),
                ('kt', models.ManyToManyField(blank=True, to='cms.kt')),
                ('last_edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_editor', to=settings.AUTH_USER_MODEL)),
                ('qtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.qtype')),
                ('role', models.ManyToManyField(blank=True, to='cms.role')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.stage')),
            ],
        ),
        migrations.AddField(
            model_name='kt',
            name='role',
            field=models.ManyToManyField(to='cms.role'),
        ),
        migrations.AddField(
            model_name='cwf',
            name='role',
            field=models.ManyToManyField(to='cms.role'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL)),
                ('mentioned', models.ManyToManyField(related_name='question_mentioned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('problem_statement', models.CharField(blank=True, max_length=1000)),
                ('remarks', models.CharField(blank=True, max_length=1000)),
                ('last_updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessment_approver', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessment_creator', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(blank=True, to='cms.question')),
                ('role', models.ManyToManyField(blank=True, to='cms.role')),
            ],
        ),
    ]
