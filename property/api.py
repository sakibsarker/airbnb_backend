from django.http import JsonResponse

from rest_framework.decorators import api_view,authentication_classes,permission_classes

from .models import Property
from .serializers import PropertiesListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    peroperties=Property.objects.all()
    serializer=PropertiesListSerializer(peroperties,many=True)

    return JsonResponse({
        'data':serializer.data
    })
