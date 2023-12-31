from rest_framework.response import Response
from . import models, serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django_filters import rest_framework as filters
from . import filters as myfilters
from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework import status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class ContinentalListView(ListAPIView):
    queryset = models.Continental.objects.all()
    serializer_class = serializers.ContinentalSerializer


class PrefixNumberListView(ListAPIView):
    queryset = models.PrefixNumber.objects.all()
    serializer_class = serializers.PrefixNumberSerializer


class CountryListCreateView(ListCreateAPIView):
    serializer_class = serializers.CountrySerializer

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
        continental = models.Continental.objects.get(pk=self.request.data.get('continental'))
        prefix_num = models.PrefixNumber.objects.get(pk=self.request.data.get('prefix_number'))
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
            return Response({'detail': f'Country \'{country.english_name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return Response({'detail': 'Country not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        continental = request.data.get('continental')
        prefix_num = request.data.get('prefix_number')
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

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Province.objects.filter(Q(name__icontains=search) | Q(english_name__icontains=search) |
                                                Q(country__name__icontains=search), deleted=False)

            return qs
        return models.Province.objects.filter(deleted=False)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.Province.objects.create(name=request.data.get('name'),
                                       english_name=request.data.get('english_name'),
                                       description=request.data.get('description'),
                                       country_id=request.data.get('country'))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProvinceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer

    def delete(self, request, *args, **kwargs):
        if models.Province.objects.filter(pk=kwargs['pk']).exists():
            province = self.get_object()
            province.deleted = True
            province.save()
            return Response({'detail': f'Province \'{province.english_name}\' has been deleted.'},
                            status=status.HTTP_200_OK)
        return Response({'detail': 'Province not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        country_id = request.data.get('country')
        if country_id:
            country = models.Country.objects.get(pk=country_id)
            instance.country = country
            instance.save()

        return super().patch(request, *args, **kwargs)


class CityListCreateView(ListCreateAPIView):
    serializer_class = serializers.CitySerializer
    filterset_class = myfilters.CityFilter

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
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')

    def delete(self, request, *args, **kwargs):
        if models.City.objects.filter(pk=kwargs['pk']).exists():
            city = self.get_object()
            city.deleted = True
            city.save()
            return Response({'detail': f'City \'{city.english_name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return Response({'detail': 'City not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        country_id = request.data.get('country')
        province_id = request.data.get('province')
        if country_id:
            country = models.Country.objects.get(pk=country_id)
            instance.country = country
        if province_id:
            province = models.Province.objects.get(pk=province_id)
            instance.province = province
        instance.save()

        return super().patch(request, *args, **kwargs)


class TerminalListCreateView(ListCreateAPIView):
    serializer_class = serializers.TerminalSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Terminal.objects.filter(Q(name__icontains=search) | Q(english_name__icontains=search) |
                                                Q(country__name__icontains=search) | Q(city__name__icontains=search) |
                                                Q(province__name__icontains=search) | Q(iata__icontains=search)
                                                , deleted=False)

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
            return Response({'detail': f'Terminal \'{terminal.english_name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return Response({'detail': 'Terminal not found.'}, status=status.HTTP_404_NOT_FOUND)


class VehicleListCreateView(ListCreateAPIView):
    serializer_class = serializers.VehicleSerializer
    filterset_class = myfilters.VehicleFilter

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Vehicle.objects.filter(Q(name__icontains=search) | Q(manufacturer__icontains=search),
                                               deleted=False)

            return qs
        return models.Vehicle.objects.filter(deleted=False)


class VehicleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer

    def delete(self, request, *args, **kwargs):
        if models.Vehicle.objects.filter(pk=kwargs['pk']).exists():
            vehicle = self.get_object()
            vehicle.deleted = True
            vehicle.save()
            return Response({'detail': f'Vehicle \'{vehicle.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)


class AccommodationListCreateView(ListCreateAPIView):
    serializer_class = serializers.AccommodationSerializer
    filterset_class = myfilters.AccommodationFilter

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Accommodation.objects.filter(Q(name__icontains=search) | Q(country__name__icontains=search)
                                                     | Q(city__name__icontains=search) | Q(
                province__name__icontains=search)
                                                     , deleted=False)

            return qs
        return models.Accommodation.objects.filter(deleted=False)


class AccommodationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Accommodation.objects.all()
    serializer_class = serializers.AccommodationSerializer

    def delete(self, request, *args, **kwargs):
        if models.Accommodation.objects.filter(pk=kwargs['pk']).exists():
            accommodation = self.get_object()
            accommodation.deleted = True
            accommodation.save()
            return Response({'detail': f'Accommodation \'{accommodation.name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return Response({'detail': 'Accommodation not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        country = models.Country.objects.get(pk=self.request.data.get('country_id'))
        province = models.Province.objects.get(pk=self.request.data.get('province_id'))
        city = models.City.objects.get(pk=self.request.data.get('city_id'))
        instance.country = country
        instance.province = province
        instance.city = city
        instance.save()
        return super().patch(request, *args, **kwargs)


class BankListCreateView(ListCreateAPIView):
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
            return Response({'detail': f'Bank \'{bank.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Bank not found.'}, status=status.HTTP_404_NOT_FOUND)


class SubscribeListCreateView(ListCreateAPIView):
    serializer_class = serializers.SubscribeSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Subscribe.objects.filter(Q(name__icontains=search) | Q(english_name__icontains=search),
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
            return Response({'detail': f'Subscribe \'{subscribe.english_name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return Response({'detail': 'Subscribe not found.'}, status=status.HTTP_404_NOT_FOUND)


class SupportListCreateView(ListCreateAPIView):
    serializer_class = serializers.SupportSerializer
    filterset_class = myfilters.SupportFilter

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.SupportType.objects.filter(Q(name__icontains=search) | Q(father__name__icontains=search),
                                                   deleted=False)

            return qs
        return models.SupportType.objects.filter(deleted=False).exclude(father=None)


class SupportRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.SupportType.objects.all()
    serializer_class = serializers.SupportSerializer

    def delete(self, request, *args, **kwargs):
        if models.SupportType.objects.filter(pk=kwargs['pk']).exists():
            support = self.get_object()
            support.deleted = True
            support.save()
            return Response({'detail': f'SupportType \'{support.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'SupportType not found.'}, status=status.HTTP_404_NOT_FOUND)


class CompanyListCreateView(ListCreateAPIView):
    serializer_class = serializers.CompanySerializer
    filterset_class = myfilters.CompanyFilter

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            qs = models.Company.objects.filter(Q(name__icontains=search) | Q(ceo__icontains=search),
                                               deleted=False)

            return qs
        return models.Company.objects.filter(deleted=False)


class CompanyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    def delete(self, request, *args, **kwargs):
        if models.Company.objects.filter(pk=kwargs['pk']).exists():
            company = self.get_object()
            company.deleted = True
            company.save()
            return Response({'detail': f'Company \'{company.name}\' has been deleted.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Company not found.'}, status=status.HTTP_404_NOT_FOUND)
