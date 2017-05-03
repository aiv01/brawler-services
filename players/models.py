from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize
from players.utilities import create_token


class Player(AbstractUser):
    photo = models.ImageField('Foto', upload_to='players/photos/')
    photo_thumb = ImageSpecField(source='photo', processors=[SmartResize(100, 100)], format='PNG', options={'quality': 100})
    audio = models.FileField('Audio', upload_to='players/audio/')
    tagline = models.CharField('Tagline', max_length=255)
    ip = models.GenericIPAddressField('Indirizzo IP', blank=True, null=True)
    port = models.SmallIntegerField('Porta', blank=True, null=True)
    registration_date = models.DateTimeField('Data di registrazione', auto_now_add=True)
    token = models.CharField('Token', max_length=36)

    def save(self, *args, **kwargs):
        # create token
        if len(self.token) < 36:
            self.token = create_token()
        super(Player, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username

Player._meta.get_field('username').verbose_name = 'Nickname'
