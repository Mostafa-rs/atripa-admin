from rest_framework import generics
from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json
from log.models import Log
from utils.functions import get_client_ip, get_client_device


class BaseApi(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)

        except Exception as e:
            Log(
                type='GET_API',
                action=request.get_full_path(),
                log=e,
                ip=get_client_ip(request),
                device=get_client_device(request)).save()
            return super().get(request, *args, **kwargs)


class ApiRenderer(BaseRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_dict = {
            'status': None,
            'errors': None,
            'data': None,
        }

        if data.get('errors') is not None or len(data.get('errors')) > 0:
            response_dict['errors'] = data.get('errors')
            response_dict['status'] = 'Error Acquired'

        else:
            response_dict['status'] = 'Success'
            response_dict['data'] = data.get('data')

        data = response_dict
        return json.dumps(data)
