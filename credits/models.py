from django.db import models
from sortable.models import PositionModel


class Role(models.Model):
    role = models.CharField('Ruolo', max_length=255)

    class Meta:
        verbose_name = 'Ruolo'
        verbose_name_plural = 'Ruoli'

    def __str__(self):
        return self.role


class Credit(PositionModel):
    name = models.CharField('Nome', max_length=255)
    surname = models.CharField('Cognome', max_length=255, blank=True, null=True)
    roles = models.ManyToManyField(Role, verbose_name='Ruoli', blank=True)
    other_info = models.TextField('Altre informazioni', blank=True, null=True)
    position = models.PositiveIntegerField('Posizione', default=0)

    @property
    def get_roles(self):
        return [str(role) for role in self.roles.all()]

    class Meta:
        verbose_name = 'Credit'
        verbose_name_plural = 'Credits'

    def __str__(self):
        return self.name
