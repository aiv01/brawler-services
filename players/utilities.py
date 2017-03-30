import hashlib
import uuid
from datetime import datetime
from base64 import b64decode
from django.utils.text import slugify
from django.core.files.base import ContentFile


def password_to_sha512(password):
    pass_sha512 = hashlib.sha512(password.encode('utf-8'))
    return pass_sha512.hexdigest()


def base64_to_png(player, photo_b64_encode):
    photo_b64_decode = b64decode(photo_b64_encode)
    player.photo = ContentFile(photo_b64_decode, '{}.png'.format(slugify(player.nickname)))
    player.save()


def create_token(nickname, password):
    token_base = nickname + password + uuid.uuid4().hex + str(datetime.now())
    token_sha512 = hashlib.sha512(token_base.encode('utf-8'))
    return token_sha512.hexdigest()
