# Generated by Django 2.2.15 on 2020-08-23 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Exam_Code', models.CharField(max_length=200)),
                ('Created_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Subject', models.TextField()),
                ('Duration', models.DurationField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('Created_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
