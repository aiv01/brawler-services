import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize


class Player(AbstractUser):
    photo = models.ImageField('Foto', upload_to='players/photos/', blank=True, null=True)
    photo_thumb = ImageSpecField(source='photo', processors=[SmartResize(100, 100)], format='PNG', options={'quality': 100})
    audio = models.FileField('Audio', upload_to='players/audio/', blank=True, null=True)
    tagline = models.CharField('Tagline', max_length=255, blank=True, null=True)
    ip = models.GenericIPAddressField('Indirizzo IP', blank=True, null=True)
    port = models.SmallIntegerField('Porta', blank=True, null=True)
    registration_date = models.DateTimeField('Data di registrazione', auto_now_add=True)
    token = models.UUIDField('Token', default=uuid.uuid4, editable=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username

Player._meta.get_field('username').verbose_name = 'Nickname'
