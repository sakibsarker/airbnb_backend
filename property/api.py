from django.http import JsonResponse

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .forms import PropertyForm
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


@api_view(['POST','FILES'])
@permission_classes([IsAuthenticated])
def create_property(request):
    form=PropertyForm(request.POST,request.FILES)
    if form.is_valid():
        property=form.save(commit=False)
        property.landlord=request.user
        property.save()
        return JsonResponse({'success':True})
    else:
        print('error',form.errors,form.non_field_errors)
        return JsonResponse({'errors':form.errors.as_json()},status=400)