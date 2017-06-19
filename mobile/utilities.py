# import socket
# import struct
from django.utils.text import slugify
from django.core.files.base import ContentFile


def bit_to_bin(model_audio, audio):
    model_audio.audio = ContentFile(audio, '{}.bin'.format(slugify(model_audio.mobile_id)))
    model_audio.save()

# def send_empower_to_server(ip, port, empower_type, server_ip, server_port):
#
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.sendto(data, (server_ip, server_port))
