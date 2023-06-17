from django.db import models


# home_team (название домашней команды), 
# away_team (название гостевой команды), home_odds (коэффициент на победу домашней команды), 
# away_odds (коэффициент на победу гостевой команды),
# draw_odds (коэффициент на ничью) и date (дата создания записи). 

class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_odds = models.DecimalField(max_digits=10, decimal_places=2)
    away_odds = models.DecimalField(max_digits=10, decimal_places=2)
    draw_odds = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team}'