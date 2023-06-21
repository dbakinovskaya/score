from django.db import models


class Seasons(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.season_name


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    search = models.CharField(max_length=3)

    def __str__(self):
        return self.country_name


class Leagues(models.Model):
    league_id = models.AutoField(primary_key=True)
    league_name = models.CharField(max_length=50)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    seasons_id = models.ForeignKey(Seasons, on_delete=models.CASCADE)

    def __str__(self):
        return self.league_name


class Fixtures(models.Model):
    fixture_id = models.AutoField(primary_key=True)
    league_id = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    home_team_id = models.IntegerField()
    away_team_id = models.IntegerField()
    date = models.DateTimeField()
    seasons_id = models.ForeignKey(Seasons, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home_team_id} vs {self.away_team_id}"


class H2H(models.Model):
    h2h_id = models.AutoField(primary_key=True)
    team1_id = models.IntegerField()
    team2_id = models.IntegerField()
    date = models.DateField()
    fixture_id = models.ForeignKey(Fixtures, on_delete=models.CASCADE)

    def __str__(self):
        return f"Match between Team {self.team1_id} and Team {self.team2_id}"


class Live(models.Model):
    live_id = models.AutoField(primary_key=True)
    fixture_id = models.ForeignKey(Fixtures, on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __str__(self):
        return f"{self.fixture_id}: {self.home_score} - {self.away_score}"


class TopScorers(models.Model):
    top_scorer_id = models.AutoField(primary_key=True)
    player_id = models.IntegerField()
    league_id = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    goals = models.IntegerField()

    def __str__(self):
        return f"{self.player_id} - {self.goals} goals"


class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=50)
    league_id = models.ForeignKey(Leagues, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class TeamStatistics(models.Model):
    team_stat_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    league_id = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    seasons_id = models.ForeignKey(Seasons, on_delete=models.CASCADE)
# надо добавить сезон?

    def __str__(self):
        return f"{self.team_id} - {self.matches_played} matches played"


class Standings(models.Model):
    standing_id = models.AutoField(primary_key=True)
    league_id = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.IntegerField()
    seasons_id = models.ForeignKey(Seasons, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_id} - {self.points} points"


class Predictions(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    fixture_id = models.ForeignKey(Fixtures, on_delete=models.CASCADE)
    home_prediction = models.FloatField()
    draw_prediction = models.FloatField()
    away_prediction = models.FloatField()

    def __str__(self):
        return f"Prediction for {self.fixture_id}"


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    fixture_id = models.ForeignKey(
        Fixtures, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_time = models.TimeField()


class Lineups(models.Model):
    lineup_id = models.AutoField(primary_key=True)
    fixture_id = models.ForeignKey(
        Fixtures, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    player_id = models.ForeignKey('players.Players', on_delete=models.CASCADE)
    position = models.CharField(max_length=50)


class MatchesStatistics(models.Model):
    match_stat_id = models.AutoField(primary_key=True)
    fixture_id = models.ForeignKey(
        Fixtures, on_delete=models.CASCADE)
    home_team_id = models.ForeignKey(
        Teams, related_name='home_team', on_delete=models.CASCADE)
    away_team_id = models.ForeignKey(
        Teams, related_name='away_team', on_delete=models.CASCADE)
    possession_home = models.FloatField()
    possession_away = models.FloatField()
    shots_home = models.IntegerField()
    shots_away = models.IntegerField()
    corners_home = models.IntegerField()
    corners_away = models.IntegerField()


class Odds(models.Model):
    odds_id = models.AutoField(primary_key=True)
    fixture_id = models.ForeignKey(
        Fixtures, on_delete=models.CASCADE)  # legue?
    bookmaker_id = models.IntegerField()
    home_odds = models.FloatField()
    draw_odds = models.FloatField()
    away_odds = models.FloatField()


class Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)


class PlayersStatistics(models.Model):
    player_stat_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    league_id = models.IntegerField()
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    fixture_id = models.ForeignKey(
        Fixtures, on_delete=models.CASCADE)#?


class PlayersTransfer(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    team_from_id = models.IntegerField()
    team_to_id = models.IntegerField()
    transfer_date = models.DateField()


class Coachs(models.Model):
    coach_id = models.AutoField(primary_key=True)
    coach_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)


class Bookmaker(models.Model):
    bookmaker_id = models.AutoField(primary_key=True)
    bookmaker_name = models.CharField(max_length=100)


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField(max_length=100)


class Trophy(models.Model):
    trophy_id = models.AutoField(primary_key=True)
    trophy_name = models.CharField(max_length=100)
    league_id = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)


class Sidelined(models.Model):
    sidelined_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
