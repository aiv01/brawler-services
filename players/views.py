from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from players.models import Player
from players.utilities import password_to_sha512, bit_to_png
from ipware.ip import get_ip


class PlayerAlreadyExistsView(View):
    def get(self, request):
        nickname = request.GET.get('nickname')
        player_already_exists = True

        try:
            Player.objects.get(nickname=nickname)
        except Player.DoesNotExist:
            player_already_exists = False

        return JsonResponse({'player_already_exists': player_already_exists})


class PlayerRegisterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerRegisterView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        tagline = request.POST.get('tagline')

        try:
            player = Player.objects.create(nickname=nickname,
                                           password=password,
                                           tagline=tagline, )
        except:
            return JsonResponse({'player_register': False,
                                 'fields': 'nickname, password, tagline',
                                 'info': 'this fields require a string of max 255 chars and nickname must be unique'})

        return JsonResponse({'player_register': True, 'token': player.token})


class PlayerLoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerLoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        ip = get_ip(request)

        password = password_to_sha512(password)
        token = None

        try:
            player = Player.objects.get(nickname=nickname,
                                        password=password, )
            token = player.token

            player.ip = ip
            player.save()

        except Player.DoesNotExist:
            return JsonResponse({'player_login': False,
                                 'fields': 'nickname, password',
                                 'info': 'wrong nickname and/or password'})

        return JsonResponse({'player_login': True, 'token': token})


class PlayerAuthView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerAuthView, self).dispatch(request, *args, **kwargs)

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
                                 'nickname': player.nickname})
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
