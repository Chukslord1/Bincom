# Generated by Django 3.0 on 2020-02-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agentname',
            fields=[
                ('name_id', models.TextField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('pollingunit_uniqueid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='announced_lga_results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=12)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='announced_pu_results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('polling_unit_uniqueid', models.IntegerField()),
                ('party_abbreviation', models.CharField(max_length=12)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='announced_state_results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='announced_ward_results',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lga',
            fields=[
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField()),
                ('lga_name', models.CharField(max_length=50)),
                ('state_id', models.IntegerField(default=25)),
                ('lga_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('partyid', models.CharField(max_length=11)),
                ('partyname', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='polling_unit',
            fields=[
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('uniqueid', models.IntegerField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField(null=True)),
                ('polling_unit_number', models.CharField(max_length=12, null=True)),
                ('polling_unit_name', models.CharField(max_length=12, null=True)),
                ('polling_unit_description', models.TextField(max_length=100, null=True)),
                ('lat', models.CharField(max_length=250, null=True)),
                ('long', models.CharField(max_length=250, null=True)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('result_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField()),
                ('state_id', models.IntegerField(default=25)),
                ('uniqueid', models.IntegerField()),
                ('party_abbreviation', models.CharField(max_length=12)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.CharField(max_length=8, null=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
    ]