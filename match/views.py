from datetime import datetime
from ipware.ip import get_ip
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from match.models import Match
from servers.models import Server
from players.models import Player


class StartMatchView(View):

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

        match = Match.objects.create(server=server)

        return JsonResponse({'start_match': True, 'id': match.id})


class AddPlayerToMatchView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AddPlayerToMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        id = request.POST.get('id')

        try:
            player = Player.objects.get(token=token)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token not found'})

        try:
            match = Match.objects.get(id=id)
        except Match.DoesNotExist:
            return JsonResponse({'error': 'match with this id not found'})

        match.participants.add(player)
        match.save()

        return JsonResponse({'player_added': True})


class EndMatchView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EndMatchView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        id = request.POST.get('id')
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            player = Player.objects.get(token=token)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token not found'})

        try:
            server = Server.objects.get(ip=ip, port=port)
        except Server.DoesNotExist:
            return JsonResponse({'error': 'server not found'})

        try:
            match = Match.objects.get(id=id, server=server)
        except Match.DoesNotExist:
            return JsonResponse({'error': 'match with this id and/or server not found'})

        try:
            match.participants.get(token=token)
        except:
            return JsonResponse({'error': 'player with this token is not a participant in this match'})

        if match.end_date:
            return JsonResponse({'error': 'this match is already over'})

        match.end_date = datetime.now()
        match.winner = player
        match.save()

        return JsonResponse({'end_match': True})
