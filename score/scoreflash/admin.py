from django.contrib import admin

from . models import (Seasons, Countries, Leagues, Fixtures, H2H, Live,
                      TopScorers, Teams, TeamStatistics, Standings, Predictions,
                      Events, MatchesStatistics, Odds, Players, PlayersStatistics,
                      PlayersTransfer, Lineups, Coachs, Bookmakers, Label, Trophy,
                      Sidelined)


models_list = [Seasons, Countries, Leagues, Fixtures, H2H, Live,
               TopScorers, Teams, TeamStatistics, Standings, Predictions,
               Events, MatchesStatistics, Odds, Players, PlayersStatistics,
               PlayersTransfer, Lineups, Coachs, Bookmakers, Label, Trophy,
               Sidelined]

for i in models_list:
    admin.site.register(i)