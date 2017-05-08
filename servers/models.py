from django.db import models
from geolite2 import geolite2


class Server(models.Model):
    ip = models.GenericIPAddressField('Indirizzo IP')
    port = models.SmallIntegerField('Porta')
    country = models.CharField('Country', max_length=255, blank=True, null=True)
    city = models.CharField('City', max_length=255, blank=True, null=True)
    time_zone = models.CharField('Time zone', max_length=255, blank=True, null=True)
    latitude = models.FloatField('Latitude', blank=True, null=True)
    longitude = models.DecimalField('Longitude', max_digits=10, decimal_places=8, blank=True, null=True)

    def save(self, *args, **kwargs):
        # save additional data
        reader = geolite2.reader()
        server = reader.get(self.ip)
        self.country = '{} ({})'.format(server['country']['names']['en'], server['country']['iso_code'])
        self.city = '{} ({})'.format(server['subdivisions'][1]['names']['en'], server['subdivisions'][1]['iso_code'])
        self.time_zone = server['location']['time_zone']
        self.latitude = server['location']['latitude']
        self.longitude = server['location']['longitude']
        reader.close()
        super(Server, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Lista server'

    def __str__(self):
        return '{}:{}'.format(self.ip, self.port)
