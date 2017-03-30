from django.views import View
from django.http import JsonResponse
from players.models import Player
from players.utilities import base64_to_png
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


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


class PlayerPhotoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlayerPhotoView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        token = request.GET.get('token')
        photo = request.body

        try:
            player = Player.objects.get(token=token)
            base64_to_png(player=player, photo_b64_encode=photo)
        except Player.DoesNotExist:
            return JsonResponse({'player_upload_photo': False,
                                 'info': 'player with this token does not exists'})

        return JsonResponse({'player_upload_photo': True})
