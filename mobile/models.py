from django.db import models


class Audio(models.Model):
    mobile_id = models.CharField('Mobile ID', max_length=255)
    audio = models.FileField('Audio')

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audio'

    def __str__(self):
        return self.mobile_id
