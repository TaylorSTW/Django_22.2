# Generated by Django 4.2.2 on 2023-07-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Preview')),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('type', models.CharField(blank=True, max_length=150, null=True, verbose_name='Type')),
                ('views_count', models.IntegerField(default=0, verbose_name='views')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]
