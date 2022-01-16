# Generated by Django 4.0.1 on 2022-01-16 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=150)),
                ('title_uz', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('WORD', 'Word'), ('PHRASE', 'Phrase')], max_length=10)),
                ('definition', models.TextField(blank=True, null=True)),
                ('audiofile', models.FileField(blank=True, null=True, upload_to='vocabulary/audio')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unit')),
            ],
        ),
    ]