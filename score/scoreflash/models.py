from django.db import models


class Seasons(models.Model):
    """Модель, которая описывает сезон игры"""
    season_name = models.CharField(
        verbose_name='Название сезона',
        max_length=50)
    start_date = models.DateField(verbose_name='Начало сезона')
    finish_date = models.DateField(verbose_name='Конец сезона')

    def __str__(self):
        return self.season_name
    
    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Countries(models.Model):
    """Модель, для описания страны"""
    country_name = models.CharField(
        verbose_name='Название страны',
        max_length=50)
    code = models.CharField(
        verbose_name='Буквенный код страны',
        max_length=2)
    # Нужно добавить флаг?
    #flag = models.ImageField(verbose_name='Флаг страны')
    search = models.CharField(max_length=3)

    def __str__(self):
        return self.country_name
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


# ========== Посмотреть подробнее про описание поля выбора (type, current) ========== #
class Leagues(models.Model):
    """Модель, для описания лиги"""
    league_name = models.CharField(
        verbose_name='Название лиги',
        max_length=50)
    country_id = models.ForeignKey(
        Countries,
        verbose_name='Код страны',
        on_delete=models.CASCADE)
    seasons_id = models.ForeignKey(
        Seasons,
        verbose_name='Код сезона',
        on_delete=models.CASCADE)
    type = models.CharField(
        verbose_name='Тип лиги',
        max_length=10, choices=[
            ("league", "League"), ("cup", "Cup")
        ]
    )
    current = models.CharField(
        verbose_name='Состояние лиги', #  Активная / не активная
        max_length=5, choices=[
            ("true", "True"), ("false", "False")
        ]
    )
    search = models.CharField(max_length=255)
    last = models.PositiveSmallIntegerField(
        verbose_name='Прошлые лиги', #  Прошлые лиги добавленные по API
    )

    def __str__(self):
        return self.league_name
    
    class Meta:
        verbose_name = 'Лига'
        verbose_name_plural = 'Лиги'


class Fixtures(models.Model):
    """Модель, для описания текущей игры"""
    seasons_id = models.ForeignKey(
        Seasons,
        verbose_name='Название сезона',
        on_delete=models.CASCADE)
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    home_team_id = models.ForeignKey(
        'Teams',
        verbose_name='Домашняя команда',
        related_name='team_home',
        on_delete=models.CASCADE)
    away_team_id = models.ForeignKey(
        'Teams',
        verbose_name='Гостевая команда',
        related_name='team_away',
        on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Дата игры')

    def __str__(self):
        return f"{self.home_team_id} vs {self.away_team_id}"
    


class H2H(models.Model):
    """Модель, для описания игры команда с командой (head to head)"""
    team1_id = models.ForeignKey(
        'Teams',
        verbose_name='Первая команда',
        related_name='team_home_h2h',
        on_delete=models.CASCADE)
    team2_id = models.ForeignKey(
        'Teams',
        verbose_name='Вторая команда',
        related_name='team_away_h2h',
        on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата игры')
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)

    def __str__(self):
        return f"Match between Team {self.team1_id} and Team {self.team2_id}"


class Live(models.Model):
    """Модель, для описания игры в режиме live"""
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    home_score = models.PositiveSmallIntegerField(
        verbose_name='Счет домашней команды')
    away_score = models.PositiveSmallIntegerField(
        verbose_name='Счет гостевой команды')

    def __str__(self):
        return f"{self.fixture_id}: {self.home_score} - {self.away_score}"


class TopScorers(models.Model):
    """Модель, для описания лучшего бомбардира"""
    player_id = models.ForeignKey(
        'Players',
        verbose_name='Лучший бомбардир',
        on_delete=models.CASCADE)
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    goals = models.PositiveSmallIntegerField(
        verbose_name='Забитые голы')

    def __str__(self):
        return f"{self.player_id} - {self.goals} goals"
    
    class Meta:
        verbose_name = 'Лучший бомбардир'
        verbose_name_plural = 'Лучшие бомбардиры'


class Teams(models.Model):
    """Модель, для описания команды"""
    team_name = models.CharField(
        verbose_name='Название команды',
        max_length=50)
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class TeamStatistics(models.Model):
    """Модель, для описания статистики команды"""
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)
    seasons_id = models.ForeignKey(
        Seasons,
        verbose_name='Название сезона',
        on_delete=models.CASCADE)
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    matches_played = models.PositiveSmallIntegerField(
        verbose_name='Количество сыгранных матчей',
    )
    wins = models.PositiveSmallIntegerField(
        verbose_name='Количество побед',
    )
    draws = models.PositiveSmallIntegerField(
        verbose_name='Количество ничьих',
    )
    losses = models.PositiveSmallIntegerField(
        verbose_name='Количество поражений',
    )
    goals_for = models.PositiveIntegerField(
        verbose_name='Голов забито',
    )
    goals_against = models.PositiveIntegerField(
        verbose_name='Голов пропущено',
    )

    def __str__(self):
        return f"{self.team_id} - {self.matches_played} matches played"
    
    class Meta:
        verbose_name = 'Статистика команды'
        verbose_name_plural = 'Статистика команды'


class Standings(models.Model):
    """Модель, для описания таблицы лиги"""
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    seasons_id = models.ForeignKey(
        Seasons,
        verbose_name='Название сезона',
        on_delete=models.CASCADE)
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)
    position = models.PositiveIntegerField(
        verbose_name='Позиция в таблице',
    )
    points = models.PositiveIntegerField(
        verbose_name='Количество очков',
    )

    def __str__(self):
        return f"{self.team_id} - {self.points} points"

    class Meta:
        verbose_name = 'Таблица лиги'
        verbose_name_plural = 'Таблица лиги'


class Predictions(models.Model):
    """Модель, для описания прогнозов"""
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    home_prediction = models.FloatField(
        verbose_name='Прогноз на победу домашней команды')
    draw_prediction = models.FloatField(
        verbose_name='Прогноз на ничью')
    away_prediction = models.FloatField(
        verbose_name='Прогноз на победу гостевой команды')

    def __str__(self):
        return f"Prediction for {self.fixture_id}"
    
    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'

# ========== Большик сомнения по поводу этой таблицы. 
# Скорее всего нужно указывать все типы событий: типы карточек, голы и т.д ========= #
class Events(models.Model):
    """Модель, для описания событий в матче"""
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)
    player_id = models.ForeignKey(
        'Players',
        verbose_name='Игрок',
        on_delete=models.CASCADE)
    event_type = models.CharField(
        verbose_name='Описание текущей игры',
        max_length=50)
    event_time = models.TimeField(
        verbose_name='Время события',
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class MatchesStatistics(models.Model):
    """Модель, для описания статистики матча"""
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    home_team_id = models.ForeignKey(
        Teams,
        verbose_name='Домашняя команда',
        related_name='team_home_stat',
        on_delete=models.CASCADE)
    away_team_id = models.ForeignKey(
        Teams,
        verbose_name='Гостевая команда',
        related_name='team_away_stat',
        on_delete=models.CASCADE)
    possession_home = models.FloatField(
        verbose_name='Владение мячом домашней команды',
    )
    possession_away = models.FloatField(
        verbose_name='Владение мячом гостевой команды',
    )
    shots_home = models.SmallIntegerField(
        verbose_name='Количество ударов в створ ворот домашней команды',
    )
    shots_away = models.SmallIntegerField(
        verbose_name='Количество ударов в створ ворот гостевой команды',
    )
    corners_home = models.SmallIntegerField(
        verbose_name='Количество угловых ударов домашней команды',
    )
    corners_away = models.SmallIntegerField(
        verbose_name='Количество угловых ударов гостевой команды',
    )

    class Meta:
        verbose_name = 'Статистика матча'
        verbose_name_plural = 'Статистика матча'


class Odds(models.Model):
    """Модель, для описания коэффициентов"""
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    bookmaker_id = models.ForeignKey(
        'Bookmakers',
        verbose_name='Букмейкер',
        on_delete=models.CASCADE)
    # home_odds = models.FloatField(
    # verbose_name='Коэффициент на победу домашней команды',)
    # draw_odds = models.FloatField(
    # verbose_name='Коэффициент на ничью',)
    # away_odds = models.FloatField(
    # verbose_name='Коэффициент на победу гостевой команды',)

    class Meta:
        verbose_name = 'Коэффициент'
        verbose_name_plural = 'Коэффициенты'


class Players(models.Model):
    """Модель, для описания игроков"""
    player_name = models.CharField(
        verbose_name='Фамилия Имя игрока',
        max_length=100)
    nationality = models.CharField(
        verbose_name='Национальность',
        max_length=50)
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
    )
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class PlayersStatistics(models.Model):
    """Модель, для описания Статистика игрока"""
    league_id = models.ForeignKey( #  Разве лига нужна?
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)
    player_id = models.ForeignKey(
        Players,
        verbose_name='Фамилия Имя игрока',
        on_delete=models.CASCADE)
    matches_played = models.SmallIntegerField(
        verbose_name='Матчей сыграно',
    )
    goals = models.SmallIntegerField(
        verbose_name='Голов забито',
    )
    assists = models.SmallIntegerField(
        verbose_name='Голевых передач',
    )

    class Meta:
        verbose_name = 'Статистика игрока'
        verbose_name_plural = 'Статистика игрока'
    


class PlayersTransfer(models.Model):
    """Модель, для описания трансфера игрока"""
    player_id = models.ForeignKey(
        Players,
        verbose_name='Фамилия Имя игрока',
        related_name='team_from',
        on_delete=models.CASCADE)
    team_from_id = models.ForeignKey(
        Teams,
        verbose_name='Команда из которой переходит',
        on_delete=models.CASCADE)
    team_to_id = models.ForeignKey(
        Teams,
        verbose_name='Команда в которую переходит',
        related_name='team_to',
        on_delete=models.CASCADE)
    transfer_date = models.DateField(
        verbose_name='Дата перехода',
    )

    class Meta:
        verbose_name = 'Трансфер игрока'
        verbose_name_plural = 'Трансфер игрока'


class Lineups(models.Model):
    """Модель, для описания состава команды в матче"""
    fixture_id = models.ForeignKey(
        Fixtures,
        verbose_name='Описание текущей игры',
        on_delete=models.CASCADE)
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)
    player_id = models.ForeignKey(
        Players,
        verbose_name='Фамилия Имя игрока',
        on_delete=models.CASCADE)
    position = models.CharField(
        verbose_name='Позиция игрока на поле',
        max_length=50)
    
    class Meta:
        verbose_name = 'Состав команды'
        verbose_name_plural = 'Состав команды'


class Coachs(models.Model):
    """Модель, для описания тренера"""
    coach_name = models.CharField(
        verbose_name='Фамилия Имя тренера',
        max_length=100)
    nationality = models.CharField(
        verbose_name='Национальность',
        max_length=100)
    team_id = models.ForeignKey(
        Teams,
        verbose_name='Команда',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Bookmakers(models.Model):
    """Модель, для описания букмемера"""
    bookmaker_name = models.CharField(
        verbose_name='Название букмекера',
        max_length=100)
    # тут на свой страх и риск связал
    odds_id = models.ForeignKey(
        Odds,
        verbose_name='Коэффициент букмекера',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Букмекер'
        verbose_name_plural = 'Букмекеры'


class Label(models.Model):
    """Модель, для описания лейбла"""
    label_name = models.CharField(
        verbose_name='Название лейбла',
        max_length=100)
    
    class Meta:
        verbose_name = 'Лейбл'
        verbose_name_plural = 'Лейблы'


class Trophy(models.Model):
    """Модель, для описания трофеев"""
    trophy_name = models.CharField(
        verbose_name='Название трофея',
        max_length=100)
    league_id = models.ForeignKey(
        Leagues,
        verbose_name='Название лиги',
        on_delete=models.CASCADE)
    player_id = models.ForeignKey(
        Players,
        verbose_name='Фамилия Имя игрока',
        on_delete=models.CASCADE)
    coahes_id = models.ForeignKey(
        Coachs,
        verbose_name='Фамилия Имя тренера',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Трофей'
        verbose_name_plural = 'Трофеи'


class Sidelined(models.Model):
    """Модель, для описания игрока, находящегося вне игры"""
    player_id = models.ForeignKey(
        Players,
        verbose_name='Фамилия Имя игрока',
        on_delete=models.CASCADE)
    reason = models.CharField(
        verbose_name='Причина',
        max_length=100)
    date_Sidelined = models.DateField(
        verbose_name='Дата удаления',
    )
    date_Inlined = models.DateField(
        verbose_name='Дата восстановления',
    )
    coahes_id = models.ForeignKey(
        Coachs,
        verbose_name='Фамилия Имя тренера',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Игрок вне игры'
        verbose_name_plural = 'Игроки вне игры'
