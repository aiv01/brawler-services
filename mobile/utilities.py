import socket
import struct
from django.utils.text import slugify
from django.core.files.base import ContentFile


def bit_to_bin(model_audio, audio):
    print('*******************')
    print(model_audio.mobile_id)
    print('*******************')
    model_audio.audio = ContentFile(audio, '{}.bin'.format(slugify(model_audio.mobile_id)))
    print('*******************')
    print(model_audio.mobile_id)
    print('*******************')
    model_audio.save()
    print('*******************')
    print(model_audio.audio.url)
    print('*******************')


def send_empower_to_server(ip, port, empower_type, server_ip, server_port):
    data = struct.pack()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(data, (server_ip, server_port))
