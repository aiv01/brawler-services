from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mobile.models import Audio
from match.models import Match
from mobile.utilities import bit_to_bin


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


class MobileMatchAudio(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MobileMatchAudio, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        mobile_id = request.GET.get('mobile_id')
        audio = request.body

        model_audio = Audio.objects.create(mobile_id=mobile_id)
        bit_to_bin(model_audio=model_audio, audio=audio)

        return JsonResponse({'mobile_upload_audio': True})


# class MobileMatchSendEmpower(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(MobileMatchSendEmpower, self).dispatch(request, *args, **kwargs)
#
#     def post(self, request):
#         mobile_id = request.POST.get('mobile_id')
#         nickname = request.POST.get('nickname')
#         empower_type = request.POST.get('empower_type')
#
#         try:
#             player = Player.objects.get(username=nickname)
#         except Player.DoesNotExist:
#             return JsonResponse({'error': 'player with this nickname not found'})
#
#         data_dict = {'EndPoint': player.ip, 'Port': player.port, 'EmpowerType': empower_type}
