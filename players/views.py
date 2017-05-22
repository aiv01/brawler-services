from datetime import datetime
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from players.models import Player, PlayerDefaultImages
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


class PlayerRegisterView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerRegisterView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        tagline = request.POST.get('tagline')
        ip = get_ip(request)

        try:
            player = Player.objects.create_user(username=nickname,
                                                password=password,
                                                tagline=tagline,
                                                ip=ip)
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
            player.last_login = datetime.now()
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
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'auth_ok': False,
                                 'fields': 'token',
                                 'info': 'player with this token does not exists'})

        if ip == player.ip:
            return JsonResponse({'auth_ok': True,
                                 'nickname': player.username})
        else:
            return JsonResponse({'auth_ok': False,
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

        print('************************************************')
        print('token --> {}'.format(token))
        print('port --> {}'.format(port))
        print('ip --> {}'.format(ip))
        print('************************************************')

        try:
            player = Player.objects.get(token=token)
        except ValidationError:
            print('************************************************')
            print("{'error': 'invalid token format'}")
            print('************************************************')

            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            print('************************************************')
            print("{'auth_ok': False, 'fields': 'token', 'info': 'player with this token does not exists'}")
            print('************************************************')
            return JsonResponse({'auth_ok': False,
                                 'fields': 'token',
                                 'info': 'player with this token does not exists'})

        if ip == player.ip:
            player.port = port
            player.save()
            print('************************************************')
            print("{'auth_ok': True}")
            print('************************************************')
            return JsonResponse({'auth_ok': True})
        else:
            print('************************************************')
            print("{'auth_ok': False, 'fields': 'ip', 'info': 'ip are not equal'}")
            print('************************************************')
            return JsonResponse({'auth_ok': False,
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
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'player_upload_photo': False,
                                 'info': 'player with this token does not exists'})

        bit_to_png(player=player, photo=photo)

        return JsonResponse({'player_upload_photo': True})


class PlayerAudioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerAudioView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.GET.get('token')
        audio = request.body

        try:
            player = Player.objects.get(token=token)
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'player_upload_audio': False,
                                 'info': 'player with this token does not exists'})

        bit_to_bin(player=player, audio=audio)

        return JsonResponse({'player_upload_audio': True})


class PlayerGetPhotoListView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerGetPhotoListView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        nickname_list = request.POST.get('nickname_list')

        nickname_list = nickname_list.split(', ')
        photo_dict = {}
        host = request.get_host()

        try:
            Player.objects.get(token=token)
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token does not exists'})

        for nickname in nickname_list:

            try:
                player = Player.objects.get(username=nickname)
            except:
                return JsonResponse({'error': 'player \'{}\' does not exists'.format(nickname)})

            try:
                photo_dict[nickname] = host + player.photo.url
            except:
                photo_dict[nickname] = None

        return JsonResponse(photo_dict)


class PlayerGetAudioListView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerGetAudioListView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        nickname_list = request.POST.get('nickname_list')

        nickname_list = nickname_list.split(', ')
        audio_dict = {}
        host = request.get_host()

        try:
            Player.objects.get(token=token)
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token does not exists'})

        for nickname in nickname_list:

            try:
                player = Player.objects.get(username=nickname)
            except:
                return JsonResponse({'error': 'player \'{}\' does not exists'.format(nickname)})

            try:
                audio_dict[nickname] = host + player.audio.url
            except:
                audio_dict[nickname] = None

        return JsonResponse(audio_dict)


class PlayerDefaultImagesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerDefaultImagesView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.POST.get('token')
        host = request.get_host()

        try:
            Player.objects.get(token=token)
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token does not exists'})

        players_default_images = PlayerDefaultImages.objects.all()
        players_default_images_list = []

        for default_image in players_default_images:
            players_default_images_dict = {}
            players_default_images_dict[default_image.title] = host + default_image.image.url
            players_default_images_dict['last_modified'] = str(default_image.last_modified)
            players_default_images_list.append(players_default_images_dict)

        return JsonResponse({'default_images': players_default_images_list})
