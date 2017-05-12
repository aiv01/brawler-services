import uuid
from django.utils.text import slugify
from django.core.files.base import ContentFile


def bit_to_png(player, photo):
    player.photo = ContentFile(photo, '{}.png'.format(slugify(player.username)))
    player.save()


def bit_to_bin(player, audio):
    player.audio = ContentFile(audio, '{}.bin'.format(slugify(player.username)))
    player.save()


def create_token():
    return uuid.uuid4()
