from django.views import View
from django.http import JsonResponse
from match.models import Match


class MobileMatchParticipants(View):

    def get(self, request):
        match = Match.objects.filter(winner=None).last()
        if match:
            participants = list(match.participants.all().values_list('username', flat=True))
            return JsonResponse({'participants': participants})
        return JsonResponse({'error': 'no match found'})
