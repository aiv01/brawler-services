from django.views import View
from django.http import JsonResponse
from players.models import Player
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
            # Save player nickname, password and tagline
            Player.objects.create(nickname=nickname,
                                  password=password,
                                  tagline=tagline, )
        except:
            return JsonResponse({'player_register': False,
                                 'fields': 'nickname, password, tagline',
                                 'info': 'this fields require a string of max 255 chars and nickname must be unique'})

        return JsonResponse({'player_register': True})
