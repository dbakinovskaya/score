# Generated by Django 2.2.16 on 2023-08-10 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BettingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('betting_type', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmaker_id', models.IntegerField()),
                ('bookmaker_name', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_event_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.TextField(null=True)),
                ('start_time', models.TextField(null=True)),
                ('start_utime', models.TextField(null=True)),
                ('game_time', models.TextField(null=True)),
                ('short_name_away', models.TextField(null=True)),
                ('away_name', models.TextField(null=True)),
                ('away_score_current', models.TextField(null=True)),
                ('away_score_part_1', models.TextField(null=True)),
                ('away_score_part_2', models.TextField(null=True)),
                ('away_images', models.URLField(null=True)),
                ('short_name_home', models.TextField(null=True)),
                ('home_name', models.TextField(null=True)),
                ('home_score_current', models.TextField(null=True)),
                ('home_score_part_1', models.TextField(null=True)),
                ('home_score_part_2', models.TextField(null=True)),
                ('home_images', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odds_label_second', models.CharField(max_length=10)),
                ('odds_label_third', models.CharField(max_length=10)),
                ('locale', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_id', models.IntegerField()),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('tournament_stage_type', models.TextField(null=True)),
                ('tournament_imng', models.TextField(null=True)),
                ('TOURNAMENT_TEMPLATE_ID', models.TextField(null=True)),
                ('TOURNAMENT_IMAGE', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField()),
                ('layout', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=100)),
                ('gender_id', models.IntegerField()),
                ('country_id', models.IntegerField()),
                ('country_name', models.CharField(max_length=100)),
                ('image_path', models.URLField()),
                ('imm', models.CharField(max_length=100)),
                ('image_width', models.IntegerField()),
                ('image_id', models.CharField(max_length=100)),
                ('ime', models.CharField(max_length=100)),
                ('image_table_path', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('type_id', models.IntegerField()),
                ('type_name', models.CharField(max_length=100)),
                ('tab', models.CharField(max_length=10)),
                ('parent_name', models.CharField(max_length=100)),
                ('actual_tournament_type', models.CharField(max_length=100)),
                ('actual_tournament_stage_id', models.CharField(max_length=100)),
                ('actual_tournament_season_id', models.CharField(max_length=100)),
                ('team_id_id', models.CharField(max_length=100)),
                ('team_participant_type', models.IntegerField()),
                ('team_image', models.ImageField(null=True, upload_to='')),
                ('team_name', models.CharField(max_length=100)),
                ('sport_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Sport')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odds_stage', models.CharField(max_length=100)),
                ('locale', models.CharField(max_length=255, null=True)),
                ('groups', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Group')),
            ],
        ),
        migrations.CreateModel(
            name='NumberOfSportEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events_count', models.IntegerField()),
                ('events_count_live', models.IntegerField()),
                ('is_popular', models.IntegerField()),
                ('sports_name', models.CharField(max_length=255, null=True)),
                ('sport_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Sport')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=255, null=True)),
                ('betting_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreflash.BettingType')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odd_cell_third_move', models.CharField(max_length=1)),
                ('odd_cell_third_value', models.FloatField()),
                ('odds_available', models.IntegerField()),
                ('locale', models.CharField(max_length=255, null=True)),
                ('bookmaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Bookmaker')),
            ],
        ),
        migrations.CreateModel(
            name='LiveOfEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('headers', models.CharField(max_length=100)),
                ('name_part_1', models.CharField(max_length=100)),
                ('name_part_2', models.CharField(max_length=100)),
                ('tournament_tamplete_id', models.CharField(max_length=100)),
                ('country_id', models.IntegerField()),
                ('country_name', models.CharField(max_length=100)),
                ('tournament_stage_id', models.CharField(max_length=100)),
                ('source_type', models.IntegerField()),
                ('has_live_table', models.IntegerField()),
                ('standing_info', models.IntegerField()),
                ('tamplate_id', models.CharField(max_length=100)),
                ('tournament_stage_type', models.IntegerField()),
                ('short_name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('tourmanet_url', models.URLField()),
                ('sort', models.CharField(max_length=100)),
                ('stage_count', models.IntegerField()),
                ('zkl', models.CharField(max_length=100)),
                ('zku', models.CharField(max_length=100)),
                ('tournamet_season_id', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Events')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='outcomes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Outcome'),
        ),
        migrations.AddField(
            model_name='bettingtype',
            name='periods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreflash.Period'),
        ),
    ]
