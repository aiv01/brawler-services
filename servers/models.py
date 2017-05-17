from django.db import models
from geolite2 import geolite2


class Server(models.Model):
    ip = models.GenericIPAddressField('Indirizzo IP')
    port = models.PositiveIntegerField('Porta')
    country = models.CharField('Country', max_length=255, blank=True, null=True)
    latitude = models.FloatField('Latitude', blank=True, null=True)
    longitude = models.FloatField('Longitude', blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            reader = geolite2.reader()
            server = reader.get(self.ip)
            self.country = '{} ({})'.format(server['country']['names']['en'], server['country']['iso_code'])
            self.latitude = server['location']['latitude']
            self.longitude = server['location']['longitude']
            reader.close()
        except:
            pass
        super(Server, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Lista server'

    def __str__(self):
        return '{}:{}'.format(self.ip, self.port)
