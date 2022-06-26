# Generated by Django 4.0.5 on 2022-06-25 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanform', '0002_added_form_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.CharField(editable=False, max_length=25, primary_key=True, serialize=False)),
                ('label', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('is_required', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('page_break', 'page_break'), ('input_field', 'input_field'), ('checkbox_field', 'checkbox_field'), ('radio_field', 'radio_field')], max_length=20)),
                ('properties', models.JSONField()),
                ('layouts', models.JSONField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_elements', to='cleanform.form')),
            ],
            options={
                'db_table': 'elements',
            },
        ),
    ]