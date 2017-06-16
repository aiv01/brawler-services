from ipware.ip import get_ip
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from servers.models import Server


class ServerRegisterView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ServerRegisterView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        ip = get_ip(request)
        port = request.POST.get('port')
        ip_2 = request.META.get('REMOTE_ADDR')

        print('*****************************')
        print(ip)
        print(ip_2)
        print('*****************************')

        try:
            Server.objects.get(ip=ip, port=port)
            return JsonResponse({'server_register': False,
                                 'fields': 'ip, port',
                                 'info': 'server already registered'})
        except:

            try:
                Server.objects.create(ip=ip, port=port)
            except:
                return JsonResponse({'server_register': False,
                                     'fields': 'ip, port',
                                     'info': 'invalid ip and/or port'})

        return JsonResponse({'server_register': True})


class ServersJsonView(View):

    def get(self, request):
        server_list = list(Server.objects.all().values('ip', 'port', 'country'))
        return JsonResponse({'servers': server_list})
