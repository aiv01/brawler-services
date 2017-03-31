from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize
from players.utilities import password_to_sha512, create_token


class Player(models.Model):
    nickname = models.CharField('Nickname', max_length=255, unique=True)
    password = models.CharField('Password', max_length=128)
    photo = models.ImageField('Foto', upload_to='players/photos/')
    photo_thumb = ImageSpecField(source='photo', processors=[SmartResize(100, 100)], format='PNG', options={'quality': 100})
    audio = models.FileField('Audio', upload_to='players/audio/')
    tagline = models.CharField('Tagline', max_length=255)
    registration_date = models.DateTimeField('Data di registrazione', auto_now_add=True)
    token = models.CharField('Token', max_length=36)

    def save(self, *args, **kwargs):
        # password to sha512
        if len(self.password) < 128:
            self.password = password_to_sha512(password=self.password)
        # create token
        if len(self.token) < 36:
            self.token = create_token()
        super(Player, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.nickname
