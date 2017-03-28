import hashlib
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize


class Player(models.Model):
    nickname = models.CharField('Nickname', max_length=255, unique=True)
    password = models.CharField('Password', max_length=255)
    photo = models.ImageField('Foto', upload_to='players/photos/')
    photo_thumb = ImageSpecField(source='photo', processors=[SmartResize(100, 100)], format='PNG', options={'quality': 100})
    audio = models.FileField('Audio', upload_to='players/audio/')
    tagline = models.CharField('Tagline', max_length=255)
    registration_date = models.DateTimeField('Data di registrazione', auto_now_add=True)

    def save(self, *args, **kwargs):
        # save password hash (sha512) and overwrite field
        pass_sha512 = hashlib.sha512(self.password.encode('utf-8'))
        self.password = pass_sha512.hexdigest()
        super(Player, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.nickname
