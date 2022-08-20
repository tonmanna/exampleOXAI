# Generated by Django 3.0.5 on 2020-09-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replies', models.TextField()),
                ('text', models.TextField()),
                ('pageID', models.IntegerField()),
                ('audienceID', models.IntegerField()),
                ('postID', models.TextField()),
                ('commentID', models.TextField()),
                ('payload', models.TextField()),
                ('attachments', models.TextField()),
                ('sentBy', models.TextField()),
                ('isReply', models.BooleanField()),
                ('createdAt', models.DateTimeField()),
                ('allowReply', models.BooleanField()),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
    ]