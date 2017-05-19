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
    port = models.PositiveIntegerField('Porta', blank=True, null=True)
    registration_date = models.DateTimeField('Data di registrazione', auto_now_add=True)
    token = models.UUIDField('Token', default=uuid.uuid4, editable=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username

Player._meta.get_field('username').verbose_name = 'Nickname'


class PlayerDefaultImages(models.Model):
    title = models.CharField('Titolo', max_length=255)
    image = models.ImageField('Immagine', upload_to='players/default-images/')
    image_thumb = ImageSpecField(source='image', processors=[SmartResize(100, 100)], format='PNG', options={'quality': 100})
    last_modified = models.DateTimeField('Ultima modifica', auto_now=True)

    class Meta:
        verbose_name = 'Immagini di default'
        verbose_name_plural = 'Immagini di default'

    def __str__(self):
        return self.title
