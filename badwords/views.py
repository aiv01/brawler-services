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
        badwords_dict = {}
        for badword in Badword.objects.all():
            badwords_dict[badword.word] = badword.replace_word
        return JsonResponse(badwords_dict)

    def post(self, request):
        token = request.POST.get('token')

        try:
            player = Player.objects.get(token=token)
        except ValidationError:
            return JsonResponse({'error': 'invalid token format'})
        except Player.DoesNotExist:
            return JsonResponse({'error': 'player with this token does not exists'})

        if player.is_staff is True:
            badwords_list = list(Badword.objects.all().values('player', 'word', 'replace_word'))
            return JsonResponse({'badwords': badwords_list})

        return JsonResponse({'error': 'access denied'})
