from django.shortcuts import render
from . import models, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django_filters import rest_framework as filters
from . import filters as myfilters
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from rest_framework import status, response
from rest_framework.views import APIView


class ContinentalListView(ListAPIView):
    queryset = models.Continental.objects.all()
    serializer_class = serializers.ContinentalSerializer


class PrefixNumberListView(ListAPIView):
    queryset = models.PrefixNumber.objects.all()
    serializer_class = serializers.PrefixNumberSerializer


class CountryListCreateView(ListCreateAPIView):
    serializer_class = serializers.CountrySerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Country.objects.filter(Q(name__icontains=search) | Q(english_name__icontains=search) |
                                               Q(continental__name__icontains=search) | Q(iata__icontains=search),
                                               deleted=False)

            return qs
        return models.Country.objects.filter(deleted=False)

    def perform_create(self, serializer):
        instance = serializer.save()
        continental = models.Continental.objects.get(pk=self.request.data.get('continental_id'))
        prefix_num = models.PrefixNumber.objects.get(pk=self.request.data.get('prefix_number_id'))
        instance.continental = continental
        instance.prefix_number = prefix_num
        instance.save()


class CountryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer

    def delete(self, request, *args, **kwargs):
        if models.Country.objects.filter(pk=kwargs['pk']).exists():
            country = self.get_object()
            country.deleted = True
            country.save()
            return JsonResponse({'detail': f'Country \'{country.english_name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Country not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        continental = request.data.get('continental_id')
        prefix_num = request.data.get('prefix_number_id')
        if continental:
            continental = models.Continental.objects.get(pk=continental)
            instance.continental = continental
            instance.save()
        if prefix_num:
            prefix_num = models.PrefixNumber.objects.get(pk=prefix_num)
            instance.prefix_number = prefix_num
            instance.save()
        return super().patch(request, *args, **kwargs)


class ProvinceListCreateView(ListCreateAPIView):
    serializer_class = serializers.ProvinceSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Province.objects.filter(Q(name__icontains=search) | Q(english_name__icontains=search) |
                                                Q(country__name__icontains=search), deleted=False)

            return qs
        return models.Province.objects.filter(deleted=False)


class ProvinceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer

    def delete(self, request, *args, **kwargs):
        if models.Province.objects.filter(pk=kwargs['pk']).exists():
            province = self.get_object()
            province.deleted = True
            province.save()
            return JsonResponse({'detail': f'Province \'{province.english_name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Province not found.'}, status=status.HTTP_404_NOT_FOUND)


class CityListCreateView(ListCreateAPIView):
    serializer_class = serializers.CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.City.objects.filter(Q(name__icontains=search) | Q(english_name__icontains=search),
                                                deleted=False)

            return qs
        return models.City.objects.filter(deleted=False)


class CityRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.City.objects.filter(deleted=False)
    serializer_class = serializers.CitySerializer
    permission_classes = [AllowAny]
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')

    def delete(self, request, *args, **kwargs):
        if models.City.objects.filter(pk=kwargs['pk']).exists():
            city = self.get_object()
            city.deleted = True
            city.save()
            return JsonResponse({'detail': f'City \'{city.english_name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'City not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        return super().patch(request, *args, **kwargs)
        # instance = models.City.objects.get(pk=kwargs['pk'])
        # instance.name = request.data['data']['name']
        # instance.save()


class TerminalListCreateView(ListCreateAPIView):
    serializer_class = serializers.TerminalSerializer

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.Country.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name')),
                                               deleted=False)

            return qs
        return models.Terminal.objects.filter(deleted=False)


class TerminalRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Terminal.objects.all()
    serializer_class = serializers.TerminalSerializer

    def delete(self, request, *args, **kwargs):
        if models.Terminal.objects.filter(pk=kwargs['pk']).exists():
            terminal = self.get_object()
            terminal.deleted = True
            terminal.save()
            return JsonResponse({'detail': f'Terminal \'{terminal.english_name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Terminal not found.'}, status=status.HTTP_404_NOT_FOUND)


class VehicleListCreateView(ListCreateAPIView):
    queryset = models.Vehicle.objects.filter(deleted=False)
    serializer_class = serializers.VehicleSerializer
    filterset_class = myfilters.VehicleFilter


class VehicleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer

    def delete(self, request, *args, **kwargs):
        if models.Vehicle.objects.filter(pk=kwargs['pk']).exists():
            vehicle = self.get_object()
            vehicle.deleted = True
            vehicle.save()
            return JsonResponse({'detail': f'Vehicle \'{vehicle.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)


class AccommodationListCreateView(ListCreateAPIView):
    queryset = models.Accommodation.objects.filter(deleted=False)
    serializer_class = serializers.AccommodationSerializer
    filterset_class = myfilters.AccommodationFilter


class AccommodationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer

    def delete(self, request, *args, **kwargs):
        if models.Accommodation.objects.filter(pk=kwargs['pk']).exists():
            accommodation = self.get_object()
            accommodation.deleted = True
            accommodation.save()
            return JsonResponse({'detail': f'Accommodation \'{accommodation.name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Accommodation not found.'}, status=status.HTTP_404_NOT_FOUND)


class BankListCreateView(ListCreateAPIView):
    queryset = models.Bank.objects.filter(deleted=False)
    serializer_class = serializers.BankSerializer
    filterset_class = myfilters.BankFilter

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            if search.isalpha():
                qs = models.Bank.objects.filter(Q(name__icontains=search),
                                                deleted=False)
            else:
                qs = models.Bank.objects.filter(Q(id=search),
                                                deleted=False)
            return qs
        return models.Bank.objects.filter(deleted=False)


class BankRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.BankSerializer

    def delete(self, request, *args, **kwargs):
        if models.Bank.objects.filter(pk=kwargs['pk']).exists():
            bank = self.get_object()
            bank.deleted = True
            bank.save()
            return JsonResponse({'detail': f'Bank \'{bank.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Bank not found.'}, status=status.HTTP_404_NOT_FOUND)


class SubscribeListCreateView(ListCreateAPIView):
    serializer_class = serializers.SubscribeSerializer

    def get_queryset(self):
        if self.request.query_params.get('name') or self.request.query_params.get('english_name'):
            qs = models.Country.objects.filter(Q(name__icontains=self.request.query_params.get('name')) |
                                               Q(english_name__icontains=self.request.query_params.get('english_name')),
                                               deleted=False)

            return qs
        return models.Subscribe.objects.filter(deleted=False)


class SubscribeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Subscribe.objects.all()
    serializer_class = serializers.SubscribeSerializer

    def delete(self, request, *args, **kwargs):
        if models.Subscribe.objects.filter(pk=kwargs['pk']).exists():
            subscribe = self.get_object()
            subscribe.deleted = True
            subscribe.save()
            return JsonResponse({'detail': f'Subscribe \'{subscribe.english_name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Subscribe not found.'}, status=status.HTTP_404_NOT_FOUND)


class SupportListCreateView(ListCreateAPIView):
    queryset = models.SupportType.objects.filter(deleted=False).exclude(father=None)
    serializer_class = serializers.SupportSerializer
    filterset_class = myfilters.SupportFilter
    

class SupportRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.SupportType.objects.all()
    serializer_class = serializers.SupportSerializer

    def delete(self, request, *args, **kwargs):
        if models.SupportType.objects.filter(pk=kwargs['pk']).exists():
            city = self.get_object()
            city.deleted = True
            city.save()
            return JsonResponse({'detail': f'SupportType \'{city.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'SupportType not found.'}, status=status.HTTP_404_NOT_FOUND)


class CompanyListCreateView(ListCreateAPIView):
    queryset = models.Company.objects.filter(deleted=False)
    serializer_class = serializers.CompanySerializer
    filterset_class = myfilters.CompanyFilter


class CompanyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    def delete(self, request, *args, **kwargs):
        if models.Company.objects.filter(pk=kwargs['pk']).exists():
            company = self.get_object()
            company.deleted = True
            company.save()
            return JsonResponse({'detail': f'Company \'{company.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Company not found.'}, status=status.HTTP_404_NOT_FOUND)



