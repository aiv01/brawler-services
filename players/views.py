from django.views import View
from django.http import JsonResponse
from players.models import Player
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File


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
        photo = request.POST.get('photo')
        audio = request.POST.get('audio')

        try:
            # Save player nickname, password and tagline
            player = Player.objects.create(nickname=nickname,
                                           password=password,
                                           tagline=tagline, )
        except:
            return JsonResponse({'player_register': False,
                                 'fields': 'nickname, password, tagline',
                                 'info': 'this fields require a string of max 255 chars and nickname must be unique'})

        try:
            # Save player photo
            photo_file = open(photo, 'rb')
            photo_django = File(photo_file)
            player.photo.save(photo.split('/')[-1], photo_django)
            photo_file.close()

            # Save player audio
            audio_file = open(audio, 'rb')
            audio_django = File(audio_file)
            player.audio.save(audio.split('/')[-1], audio_django)
            audio_file.close()
        except:
            return JsonResponse({'player_register': False,
                                 'fields': 'photo, audio',
                                 'info': 'use \'/\' for path and make sure it is correct'})

        return JsonResponse({'player_register': True})
