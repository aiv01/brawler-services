from django.views import View
from django.http import JsonResponse
from credits.models import Credit


class CreditJsonView(View):

    def get_credits(self):
        credits = Credit.objects.all().order_by('position')
        credits_list = []
        for credit in credits:
            credits_list.append({'name': credit.name, 'surname': credit.surname,
                                 'roles': credit.get_roles, 'other_info': credit.other_info})
        return credits_list

    def get(self, request):
        return JsonResponse({'credits': self.get_credits()})
