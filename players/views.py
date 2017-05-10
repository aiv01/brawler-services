from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from players.models import Player
from players.utilities import create_token, bit_to_png, bit_to_bin
from ipware.ip import get_ip


class PlayerAlreadyExistsView(View):

    def get(self, request):
        nickname = request.GET.get('nickname')
        player_already_exists = True

        try:
            Player.objects.get(username=nickname)
        except Player.DoesNotExist:
            player_already_exists = False

        return JsonResponse({'player_already_exists': player_already_exists})


class PlayerGetPhotoView(View):

    def get(self, request):
        nickname = request.GET.get('nickname')

        host = request.get_host()
        photo = None

        try:
            player = Player.objects.get(username=nickname)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this nickname does not exists'})

        if player.photo:
            photo = host + player.photo.url

        return JsonResponse({'photo': photo})


class PlayerGetAudioView(View):

    def get(self, request):
        nickname = request.GET.get('nickname')

        host = request.get_host()
        audio = None

        try:
            player = Player.objects.get(username=nickname)
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this nickname does not exists'})

        if player.audio:
            audio = host + player.audio.url

        return JsonResponse({'audio': audio})


class PlayerRegisterView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerRegisterView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        tagline = request.POST.get('tagline')

        try:
            player = Player.objects.create_user(username=nickname,
                                                password=password,
                                                tagline=tagline)
        except:
            return JsonResponse({'player_register': False,
                                 'fields': 'nickname, password, tagline',
                                 'info': 'password and tagline require a string of max 255 chars. Nickname must be unique and require a string of max 150 chars'})

        return JsonResponse({'player_register': True, 'token': player.token})


class PlayerLoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerLoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        ip = get_ip(request)

        try:
            player = authenticate(username=nickname, password=password)

            player.token = create_token()
            player.ip = ip
            player.save()

        except:
            return JsonResponse({'player_login': False,
                                 'fields': 'nickname, password',
                                 'info': 'wrong nickname and/or password'})

        return JsonResponse({'player_login': True, 'token': player.token})


class PlayerServerAuthView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerServerAuthView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        ip = request.POST.get('ip')

        try:
            player = Player.objects.get(token=token)

        except Player.DoesNotExist:
            return JsonResponse({'auth_ok': False,
                                 'fields': 'token',
                                 'info': 'player with this token does not exists'})

        if ip == player.ip:
            return JsonResponse({'auth_ok': True,
                                 'nickname': player.username})
        else:
            return JsonResponse({'aut_ok': False,
                                 'fields': 'ip',
                                 'info': 'ip are not equal'})


class PlayerClientAuthView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerClientAuthView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        port = request.POST.get('port')
        ip = get_ip(request)

        try:
            player = Player.objects.get(token=token)

        except Player.DoesNotExist:
            return JsonResponse({'auth_ok': False,
                                 'fields': 'token',
                                 'info': 'player with this token does not exists'})

        if ip == player.ip:
            player.port = port
            player.save()
            return JsonResponse({'auth_ok': True})
        else:
            return JsonResponse({'aut_ok': False,
                                 'fields': 'ip',
                                 'info': 'ip are not equal'})


class PlayerPhotoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerPhotoView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.GET.get('token')
        photo = request.body

        try:
            player = Player.objects.get(token=token)
            bit_to_png(player=player, photo=photo)

        except Player.DoesNotExist:
            return JsonResponse({'player_upload_photo': False,
                                 'info': 'player with this token does not exists'})

        return JsonResponse({'player_upload_photo': True})


class PlayerAudioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerAudioView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        audio = request.body

        try:
            player = Player.objects.get(token=token)
            bit_to_bin(player=player, audio=audio)

        except Player.DoesNotExist:
            return JsonResponse({'player_upload_audio': False,
                                 'info': 'player with this token does not exists'})

        return JsonResponse({'player_upload_audio': True})
