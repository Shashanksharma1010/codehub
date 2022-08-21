# Generated by Django 3.2.7 on 2021-09-25 08:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codeblog', '0002_alter_post_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='code',
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('code', ckeditor.fields.RichTextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeblog.post')),
            ],
        ),
    ]
