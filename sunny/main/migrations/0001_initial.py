# Generated by Django 3.2.5 on 2023-07-17 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion_Image',
            fields=[
                ('champion_eng_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('champion_kor_name', models.CharField(max_length=50)),
                ('champion_icon_image', models.ImageField(upload_to='images/champion_icon/')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Image',
            fields=[
                ('item_code', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('item_image', models.ImageField(upload_to='images/item/')),
            ],
        ),
        migrations.CreateModel(
            name='League_Entries',
            fields=[
                ('league_entries_id', models.AutoField(primary_key=True, serialize=False)),
                ('leagueId', models.CharField(max_length=255)),
                ('queueType', models.CharField(max_length=255)),
                ('tier', models.CharField(max_length=255)),
                ('rank', models.CharField(max_length=255)),
                ('summonerName', models.CharField(max_length=255)),
                ('leaguePoints', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('totalGames', models.IntegerField()),
                ('winRate', models.FloatField()),
                ('veteran', models.BooleanField()),
                ('inactive', models.BooleanField()),
                ('freshBlood', models.BooleanField()),
                ('hotStreak', models.BooleanField()),
                ('miniSeries', models.JSONField(null=True)),
                ('summonerId', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Perk_Image',
            fields=[
                ('main_perk_id', models.IntegerField(primary_key=True, serialize=False)),
                ('main_perk_name', models.CharField(max_length=255)),
                ('main_perk_image', models.ImageField(upload_to='images/main_perk/')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('metadata', models.JSONField()),
                ('info', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='MatchId',
            fields=[
                ('matchId', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Spell_Image',
            fields=[
                ('spell_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('spell_name', models.CharField(max_length=50)),
                ('spell_key', models.CharField(max_length=3)),
                ('spell_image', models.ImageField(upload_to='images/spell/')),
            ],
        ),
        migrations.CreateModel(
            name='Summoner_Info',
            fields=[
                ('summonerId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('accountId', models.CharField(max_length=255)),
                ('puuid', models.CharField(max_length=255)),
                ('summonerName', models.CharField(max_length=255)),
                ('profileIconId', models.IntegerField()),
                ('revisionDate', models.BigIntegerField()),
                ('summonerLevel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Time_Info',
            fields=[
                ('time_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('split_startTime', models.DateTimeField()),
                ('currentTime', models.DateTimeField()),
                ('split_startTime_unix', models.IntegerField()),
                ('currentTime_unix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SummonerId_MatchId',
            fields=[
                ('summonerId_matchId_id', models.AutoField(primary_key=True, serialize=False)),
                ('gameCreation', models.BigIntegerField()),
                ('matchId', models.ForeignKey(db_column='matchId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.matchid')),
                ('summonerId', models.ForeignKey(db_column='summonerId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.summoner_info')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Perk_Image',
            fields=[
                ('sub_perk_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sub_perk_name', models.CharField(max_length=255)),
                ('sub_perk_image', models.ImageField(upload_to='images/sub_perk/')),
                ('main_perk_id', models.ForeignKey(db_column='main_perk_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.main_perk_image')),
            ],
        ),
        migrations.CreateModel(
            name='Match_Metadata',
            fields=[
                ('match_metadata_id', models.AutoField(primary_key=True, serialize=False)),
                ('dataVersion', models.CharField(max_length=50)),
                ('participants', models.JSONField()),
                ('matchId', models.ForeignKey(db_column='matchId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.matchid')),
                ('match_id', models.ForeignKey(db_column='match_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.match')),
            ],
        ),
        migrations.CreateModel(
            name='Match_Info',
            fields=[
                ('gameCreation', models.BigIntegerField()),
                ('gameDuration', models.IntegerField()),
                ('gameEndTimestamp', models.BigIntegerField()),
                ('gameId', models.BigIntegerField(primary_key=True, serialize=False)),
                ('gameMode', models.CharField(max_length=50)),
                ('gameName', models.CharField(max_length=50)),
                ('gameStartTimestamp', models.BigIntegerField()),
                ('gameType', models.CharField(max_length=50)),
                ('gameVersion', models.CharField(max_length=50)),
                ('mapId', models.IntegerField()),
                ('participants', models.JSONField()),
                ('platformId', models.CharField(max_length=50)),
                ('queueId', models.IntegerField()),
                ('teams', models.JSONField()),
                ('tournamentCode', models.CharField(max_length=50)),
                ('matchId', models.ForeignKey(db_column='matchId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.matchid')),
                ('match_id', models.ForeignKey(db_column='match_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.match')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='matchId',
            field=models.ForeignKey(db_column='matchId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.matchid'),
        ),
        migrations.CreateModel(
            name='League_Info',
            fields=[
                ('league_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('leagueId', models.CharField(max_length=255)),
                ('queueType', models.CharField(max_length=255)),
                ('tier', models.CharField(max_length=255)),
                ('rank', models.CharField(max_length=255)),
                ('summonerName', models.CharField(max_length=255)),
                ('leaguePoints', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('totalGames', models.IntegerField()),
                ('winRate', models.FloatField()),
                ('veteran', models.BooleanField()),
                ('inactive', models.BooleanField()),
                ('freshBlood', models.BooleanField()),
                ('hotStreak', models.BooleanField()),
                ('summonerId', models.ForeignKey(db_column='summonerId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.summoner_info')),
            ],
        ),
    ]