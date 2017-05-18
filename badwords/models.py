from django.db import models
from players.models import Player


class Badword(models.Model):
    word = models.CharField('Parola', max_length=255, unique=True, help_text='Case insensitive')
    player = models.ForeignKey(Player, verbose_name='Player', blank=True, null=True)

    def clean(self):
        self.word = self.word.lower()

    class Meta:
        verbose_name = 'Badword'
        verbose_name_plural = 'Lista badwords'

    def __str__(self):
        return self.word
