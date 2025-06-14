# Generated by Django 5.0.6 on 2025-06-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_membres', '0033_member_blocked_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilNonValide',
            fields=[
            ],
            options={
                'verbose_name': 'Profil non validé',
                'verbose_name_plural': 'Profils non validés',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app_membres.profil',),
        ),
        migrations.CreateModel(
            name='ProfilValide',
            fields=[
            ],
            options={
                'verbose_name': 'Profil validé',
                'verbose_name_plural': 'Profils validés',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app_membres.profil',),
        ),
    ]
