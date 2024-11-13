from django.http import JsonResponse

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .forms import PropertyForm
from .models import Property,Reservation
from .serializers import PropertiesListSerializer,PropertiesDetailsSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    peroperties=Property.objects.all()
    serializer=PropertiesListSerializer(peroperties,many=True)

    return JsonResponse({
        'data':serializer.data
    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_detail(request,pk):
    property=Property.objects.get(pk=pk)
    serializer=PropertiesDetailsSerializer(property,many=False)

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_property(request,pk):
    try:
        start_date=request.POST.get("start_date","")
        end_date=request.POST.get("end_date","")
        number_of_nights=request.POST.get("number_of_nights","")
        total_price=request.POST.get("total_price","")
        guests=request.POST.get("guests","")

        property=Property.objects.get(pk=pk)


        Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            number_of_nights=number_of_nights,
            total_price=total_price,
            guests=guests,
            created_by=request.user

        )

        return JsonResponse({"success":True})
    
    except Exception as e:
        print('Error',e)

        return JsonResponse({"success":False})