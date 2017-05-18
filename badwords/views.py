from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from badwords.models import Badword
from players.models import Player


class BadwordJsonView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BadwordJsonView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        badwords_list = list(Badword.objects.all().values_list('word', flat=True))
        return JsonResponse({'badwords': badwords_list})

    def post(self, request):
        token = request.POST.get('token')

        try:
            player = Player.objects.get(token=token)
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token does not exists'})

        if player.is_staff is True:
            badwords_list = list(Badword.objects.all().values('player', 'word'))
            return JsonResponse({'badwords': badwords_list})

        return JsonResponse({'error': 'access denied'})
