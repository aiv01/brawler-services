from django.utils.text import slugify
from django.core.files.base import ContentFile


def bit_to_png(match, image):
    match.winner_img = ContentFile(image, '{}.png'.format(slugify(match.winner.username)))
    match.save()
