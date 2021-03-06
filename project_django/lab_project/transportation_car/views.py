from datetime import datetime, date, timedelta

from django.db.models.functions import Coalesce
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Transportation, Location
from .serializers import TransportationSerializer
from .forms import AddTransportations, AddressForm, TransportationForm, FindTransportForm, User, FindTransportationsDataCreatedForm
from account.forms import ProfileForm
from account.models import Profile


def main(request):
    return render(request=request, template_name='transportation_car/main.html')


def index(request, ile):
    form = FindTransportForm()
    if 'start' and 'end' in request.GET:
        form = FindTransportForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            transportations = Transportation.objects.filter(start_location=cd['start'])
    else:
        # transportations = Transportation.objects.all().order_by('data_created').desc()
        transportations = Transportation.objects.all().order_by('-data_created')
        print(type(transportations))
        context = {
            'transportations': transportations[10*(ile-1):10*ile],
            'length': transportations.count(),
            'number': ile,
        }
        return render(request=request, template_name='transportation_car/index.html', context=context)


def transportationId(request, id):
    transportation = Transportation.objects.get(pk=id)
    context = {
        'transportation': transportation,
    }
    return render(request=request, template_name='transportation_car/transportation.html', context=context)

def getUserOrder(request, user_id, ile, date1,date2):
    # if request.method == 'GET':
    date_1 = datetime.strptime(date1, '%Y-%m-%d')
    date_2 = datetime.strptime(date2, '%Y-%m-%d')
    new_end = date_2 + timedelta(days=1)
    transportations = Transportation.objects.filter(car_owner=user_id, data_created__range=[date_1, new_end]).order_by('-data_created')
    form = FindTransportationsDataCreatedForm()

    context = {
        'transportations': transportations[10*(ile-1):10*ile],
        'length': transportations.count(),
        'number': ile,
        'form': form,
        'date1': str(date_1),
        'date2': str(date_2),
    }
    return render(request=request, template_name='transportation_car/my_orders.html', context=context)

def deleteTransportId(request, id):
    transportation = Transportation.objects.get(pk=id)
    transportation.delete()
    user = User.objects.get(pk=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    form_change_photo = ProfileForm()
    transportations = Transportation.objects.filter(car_owner=request.user.id).order_by('-data_created')
    context = {
    }
    return render(request, 'transportation_car/home.html', context)

def editTransportId(request, id):
    transportation = Transportation.objects.get(pk=id)
    # user = User.objects.get(pk=request.user.id)
    # profile = Profile.objects.get(user_id=request.user.id)
    form = TransportationForm()
    transportations = Transportation.objects.filter(car_owner=request.user.id).order_by('-data_created')
    context = {
        'form': form,
        'transportations': transportations,
    }
    return render(request, 'transportation_car/create_transportations.html', context)


class getTransportations(generics.ListCreateAPIView):
    # queryset = Transportation.objects.all()
    queryset = Transportation.objects.all().order_by('-data_created')
    serializer_class = TransportationSerializer


class getTransportationId(generics.ListCreateAPIView):
    serializer_class = TransportationSerializer

    def get_queryset(self, **kwargs):
        user_id = int(self.kwargs['user_id'])
        # user = User.objects.get(pk=user_id)
        # model_instance = Profile.objects.get_or_create(user=user)
        return Transportation.objects.filter(car_owner=self.kwargs['user_id']).order_by('-data_created')


class TransportAPI(APIView):

    def get_object(self, pk):
        try:
            return Transportation.objects.get(pk=pk)
        except Transportation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transport = self.get_object(pk)
        serializer = TransportationSerializer(transport)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



def create_transportations(request):
    if request.method == 'POST':
        form = TransportationForm(request.POST)
        form.car_owner = request.user.username
        print(request.user.username)
        print(form.car_owner)
        if form.is_valid():
            # cd = form.cleaned_data
            # user = authenticate(username=cd['username'], password=cd['password'])
            new_transportation = form.save(commit=False)
            new_transportation.car_owner = request.user
            if request.FILES:
                new_transportation.photo = request.FILES['photo']
            new_transportation.save()
            # transportations = Transportation.objects.all()
            transportations = Transportation.objects.all().order_by('-data_created')
            context = {
                'transportations': transportations
            }
            return render(request=request, template_name='transportation_car/main.html', context=context)
            # return render(request, 'account/register_done.html', {'new_user': "new_user"})
        else:
            return render(request, 'account/invalid_data.html', {'error': 'Invalid data!!!'})
            # return HttpResponse('Invalid login')
    else:
        form = TransportationForm()
    return render(request, 'transportation_car/create_transportations.html', {'form': form})





