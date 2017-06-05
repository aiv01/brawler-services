from django.db import models
from players.models import Player


class Match(models.Model):
    date = models.DateTimeField('Data', auto_now_add=True)
    participants = models.ManyToManyField(Player, verbose_name='Partecipanti', related_name='match_participants', blank=True)
    winner = models.ForeignKey(Player, verbose_name='Vincitore', related_name='match_winner', blank=True, null=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Match'

    def __str__(self):
        return self.id
