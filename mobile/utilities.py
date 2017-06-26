import struct
import time
import json
import socket
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


class SendEmpower:
    empower_id = 0

    def send_empower_to_server(ip, port, empower_type, server_ip, server_port):
        SendEmpower.empower_id += 1

        empower_dict = {'Ip': ip, 'Port': port, 'EmpowerType': empower_type}
        empower_json = json.dumps(empower_dict)
        empower_b = empower_json.encode('utf-8')
        empower_len = len(empower_b)

        header = struct.pack('<IIBB', SendEmpower.empower_id, int(time.time()), 100, empower_len)

        data = b''.join([header, empower_b])

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(data, (server_ip, server_port))


class SendMessage:
    message_id = 0

    def send_message_to_server(mobile_name, text, server_ip, server_port):
        SendMessage.message_id += 1

        message_dict = {'Name': mobile_name, 'Text': text}
        message_json = json.dumps(message_dict)
        message_b = message_json.encode('utf-8')
        message_len = len(message_b)

        header = struct.pack('<IIBB', SendMessage.message_id, int(time.time()), 123, message_len)

        data = b''.join([header, message_b])

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(data, (server_ip, server_port))
