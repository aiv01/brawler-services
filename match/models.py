from django.db import models
from servers.models import Server
from players.models import Player


class Match(models.Model):
    start_date = models.DateTimeField('Start', auto_now_add=True)
    end_date = models.DateTimeField('End', blank=True, null=True)
    server = models.ForeignKey(Server, verbose_name='Server', blank=True, null=True)
    participants = models.ManyToManyField(Player, verbose_name='Partecipanti', related_name='match_participants', blank=True)
    winner = models.ForeignKey(Player, verbose_name='Vincitore', related_name='match_winner', blank=True, null=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Match'

    def __str__(self):
        return str(self.id)
