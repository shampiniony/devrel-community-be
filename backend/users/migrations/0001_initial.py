# Generated by Django 5.0 on 2023-12-15 23:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Навыки')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Специализация')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('city', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Город')),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('grade', models.CharField(blank=True, choices=[('intern', 'Intern'), ('apprentice', 'Apprentice'), ('junior', 'Junior Developer'), ('mid', 'Mid-level Developer'), ('senior', 'Senior Developer'), ('lead', 'Lead Developer'), ('principal', 'Principal Developer'), ('architect', 'Architect'), ('tech_lead', 'Tech Lead'), ('engineering_manager', 'Engineering Manager'), ('chief_architect', 'Chief Architect')], max_length=20, verbose_name='Ступень')),
                ('work_experience', models.PositiveIntegerField(default=0, verbose_name='Опыт работы (в годах)')),
                ('is_devrel', models.BooleanField(default=False, verbose_name='DevRel')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('skills', models.ManyToManyField(blank=True, related_name='users', to='users.skill', verbose_name='Навыки')),
                ('specializations', models.ManyToManyField(blank=True, related_name='users', to='users.specialization', verbose_name='Специализации')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
