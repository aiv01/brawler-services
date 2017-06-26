from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mobile.models import Audio
from match.models import Match
from mobile.utilities import bit_to_bin
from mobile.utilities import SendEmpower, SendMessage


class MobileMatchParticipants(View):

    def get(self, request):
        match = Match.objects.filter(winner=None).last()
        host = request.get_host()

        if match:
            participants = list(match.participants.all().values_list('username', flat=True))
            participants_dict = {}

            for participant in participants:

                try:
                    photo = match.participants.get(username=participant).photo.url
                    photo = host + photo
                except ValueError:
                    photo = None

                participants_dict[participant] = photo

            return JsonResponse(participants_dict)

        return JsonResponse({'error': 'no match found'})


class MobileMatchSendEmpower(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MobileMatchSendEmpower, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        mobile_id = request.POST.get('mobile_id')
        nickname = request.POST.get('nickname')
        empower_type = int(request.POST.get('empower_type'))

        try:
            match = Match.objects.filter(winner=None).last()
            print(match)
        except Match.DoesNotExist:
            return JsonResponse({'error': 'match not found'})

        try:
            player = match.participants.get(username=nickname)
            print(player)
        except:
            return JsonResponse({'error': 'player with this nickname not found'})

        SendEmpower.send_empower_to_server(player.ip, player.port, empower_type, match.server.ip, match.server.port)
        return JsonResponse({'send_empower': True})


class MobileMatchSendMessage(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MobileMatchSendMessage, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        mobile_id = request.POST.get('mobile_id')
        mobile_name = request.POST.get('mobile_name')
        text = request.POST.get('text')

        try:
            match = Match.objects.filter(winner=None).last()
            print(match)
        except Match.DoesNotExist:
            return JsonResponse({'error': 'match not found'})

        SendMessage.send_message_to_server(mobile_name, text, match.server.ip, match.server.port)
        return JsonResponse({'send_message': True})


class MobileMatchAudio(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MobileMatchAudio, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        mobile_id = request.GET.get('mobile_id')
        print('********************************')
        print(mobile_id)
        print('********************************')
        audio = request.body
        print('********************************')
        print(audio)
        print('********************************')

        model_audio = Audio.objects.create(mobile_id=mobile_id)
        bit_to_bin(model_audio=model_audio, audio=audio)

        return JsonResponse({'mobile_upload_audio': True})
