from django.views import View
from django.http import JsonResponse
from match.models import Match


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
