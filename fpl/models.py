from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings



class PlayerStats(models.Model):
    full_name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100, unique=True)
    total_goals = models.IntegerField(max_length=100)
    assists = models.IntegerField(max_length=100)
    assists_home = models.IntegerField(max_length=100)
    assists_away = models.IntegerField(max_length=100)
    goals_home = models.IntegerField(max_length=100)
    goals_away = models.IntegerField(max_length=100)
    clean_sheets = models.IntegerField(max_length=100)
    goals_per_90_overall = models.FloatField(max_length=100)
    goals_per_90_home = models.FloatField(max_length=100)
    goals_per_90_away = models.FloatField(max_length=100)
    penalty_goals = models.IntegerField(max_length=100)
    minutes_played_overall = models.IntegerField(max_length=100)
