from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.http import HttpResponse

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from oscar.apps.catalogue.models import Product
from rest_framework.decorators import authentication_classes, permission_classes
from django.views.decorators.http import require_GET
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def HelloWorld(request):
    try:
        return JsonResponse("Hello World!", safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@require_GET
def Products(request):
    # if request.user:
        # fcmdevice.user = request.user
        # fcmdevice.save()
    products = list(Product.objects.all().values())
    # return JsonResponse({'products': list(products)})
    return HttpResponse(json.dumps(products, cls=DjangoJSONEncoder), content_type='application/json')

    # return JsonResponse(products, safe=False)

    # logger.info("User {} registred new device token '{}'".format(request.user, token))
    # return HttpResponse('{"success": true } \n', content_type="application/json")
