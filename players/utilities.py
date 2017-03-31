import hashlib
import uuid
from django.utils.text import slugify
from django.core.files.base import ContentFile


def password_to_sha512(password):
    pass_sha512 = hashlib.sha512(password.encode('utf-8'))
    return pass_sha512.hexdigest()


def bit_to_png(player, photo):
    player.photo = ContentFile(photo, '{}.png'.format(slugify(player.nickname)))
    player.save()


def create_token():
    return str(uuid.uuid4())
