from datetime import datetime
from ipware.ip import get_ip
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from match.models import Room, Match
from servers.models import Server
from players.models import Player
from match.utilities import bit_to_png


class AddRoomView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StartMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            server = Server.objects.get(ip=ip, port=port)
        except Server.DoesNotExist:
            return JsonResponse({'error': 'server not found'})

        room = Room.objects.create(server=server)

        return JsonResponse({'room_added': True, 'id': room.id})


class ResetRoomView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ResetRoomView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        id = request.POST.get('id')
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            server = Server.objects.get(ip=ip, port=port)
        except Server.DoesNotExist:
            return JsonResponse({'error': 'server not found'})

        try:
            room = Room.objects.get(id=id, server=server)
        except Room.DoesNotExist:
            return JsonResponse({'error': 'match with this id and/or server not found'})

        room.participants.all().delete()
        room.lobby = True
        room.save()

        return JsonResponse({'room_added': True, 'id': room.id})


class AddPlayerToRoomView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AddPlayerToRoomView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        id = request.POST.get('id')
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            player = Player.objects.get(username=nickname)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this nickname not found'})

        try:
            server = Server.objects.get(ip=ip, port=port)
        except Server.DoesNotExist:
            return JsonResponse({'error': 'server not found'})

        try:
            room = Room.objects.get(id=id, server=server)
        except Room.DoesNotExist:
            return JsonResponse({'error': 'match with this id and/or server not found'})

        room.participants.add(player)
        room.save()

        return JsonResponse({'player_added': True})


class RoomListView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RoomListView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')

        try:
            Player.objects.get(token=token)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token not found'})

        room_list = []
        for room in Room.objects.all():
            room_dict = {}
            room_dict['id'] = room.id
            room_dict['lobby'] = room.lobby
            room_dict['participants'] = list(room.participants.all().values_list('username', flat=True))
            room_list.append(room_dict)

        return JsonResponse({'room_list': room_list})


class StartMatchView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StartMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        room_id = request.POST.get('room_id')
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            server = Server.objects.get(ip=ip, port=port)
        except Server.DoesNotExist:
            return JsonResponse({'error': 'server not found'})

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return JsonResponse({'error': 'room with this id not found'})

        match = Match.objects.create(server=server)

        for player in room.participants.all():
            match.participants.add(player)
        match.save()

        room.lobby = False

        return JsonResponse({'start_match': True, 'id': match.id})


class EndMatchView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EndMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        id = request.POST.get('id')
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            player = Player.objects.get(username=nickname)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this nickname not found'})

        try:
            server = Server.objects.get(ip=ip, port=port)
        except Server.DoesNotExist:
            return JsonResponse({'error': 'server not found'})

        try:
            match = Match.objects.get(id=id, server=server)
        except Match.DoesNotExist:
            return JsonResponse({'error': 'match with this id and/or server not found'})

        try:
            match.participants.get(username=nickname)
        except:
            return JsonResponse({'error': 'player with this nickname is not a participant in this match'})

        if match.end_date:
            return JsonResponse({'error': 'this match is already over'})

        match.end_date = datetime.now()
        match.winner = player
        match.save()

        return JsonResponse({'end_match': True})


class WinnerImgView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WinnerImgView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        match_id = request.GET.get('match_id')
        token = request.GET.get('token')
        winner_img = request.body

        try:
            match = Match.objects.get(id=match_id)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'match not found'})

        if token != match.player.token:
            return JsonResponse({'error': 'wrong winner'})

        bit_to_png(match, winner_img)
        return JsonResponse({'winner_img_upload': True})
