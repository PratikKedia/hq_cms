# Generated by Django 4.0.5 on 2022-06-09 04:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_comment_question_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='mentioned',
            field=models.ManyToManyField(related_name='question_mentioned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='comment',
            field=models.ManyToManyField(blank=True, to='cms.comment'),
        ),
    ]
