from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models, serializers
from rest_framework.permissions import AllowAny


class RewardListCreateView(ListCreateAPIView):
    queryset = models.Reward.objects.all().exclude(deleted=True)
    serializer_class = serializers.RewardListSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        new_usages = self.request.data.get('usages')
        category_id = self.request.data.get('category_id')
        category = models.RewardCategory.objects.get(pk=category_id)
        instance = serializer.save()
        if category:
            instance.category = category
            instance.save()
        if new_usages:
            usages = instance.cru_reward
            for k in new_usages.keys():
                if k == 'all':
                    usages.all = True
                elif k == 'all_transport':
                    usages.all_transport = True
                elif k == 'accommodation_all':
                    usages.accommodation_all = True
                elif k == 'tour_all':
                    usages.tour_all = True
                elif k == 'subscribe_low_all':
                    usages.subscribe_low_all = True
                elif k == 'subscribe_med_all':
                    usages.subscribe_med_all = True
                elif k == 'subscribe_high_all':
                    usages.subscribe_high_all = True
                elif k == 'airplane':
                    usages.airplane = True
                elif k == 'bus':
                    usages.bus = True
                elif k == 'train':
                    usages.train = True
                elif k == 'hotel':
                    usages.hotel = True
                elif k == 'other_accommodation':
                    usages.other_accommodation = True
                elif k == 'tour':
                    usages.tour = True
                elif k == 'subscribe_low_one_month':
                    usages.subscribe_low_one_month = True
                elif k == 'subscribe_med_one_month':
                    usages.subscribe_med_one_month = True
                elif k == 'subscribe_high_one_month':
                    usages.subscribe_high_one_month = True
                elif k == 'subscribe_low_three_month':
                    usages.subscribe_low_three_month = True
                elif k == 'subscribe_med_three_month':
                    usages.subscribe_med_three_month = True
                elif k == 'subscribe_high_three_month':
                    usages.subscribe_high_three_month = True
                elif k == 'subscribe_low_six_month':
                    usages.subscribe_low_six_month = True
                elif k == 'subscribe_med_six_month':
                    usages.subscribe_med_six_month = True
                elif k == 'subscribe_high_six_month':
                    usages.subscribe_high_six_month = True
                elif k == 'subscribe_low_one_year':
                    usages.subscribe_low_one_year = True
                elif k == 'subscribe_med_one_year':
                    usages.subscribe_med_one_year = True
                elif k == 'subscribe_high_one_year':
                    usages.subscribe_high_one_year = True
                usages.save()


class RewardRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Reward.objects.all()
    serializer_class = serializers.RewardSerializer
    
    def patch(self, request, *args, **kwargs):
        new_usages = request.data.get('usages')
        category_id = self.request.data.get('category_id')
        category = models.RewardCategory.objects.get(pk=category_id)
        instance = self.get_object()
        if category:
            instance.category = category
            instance.save()
        if new_usages:
            usages = instance.cru_reward
            for k in new_usages.keys():
                if k == 'all':
                    usages.all = True
                elif k == 'all_transport':
                    usages.all_transport = True
                elif k == 'accommodation_all':
                    usages.accommodation_all = True
                elif k == 'tour_all':
                    usages.tour_all = True
                elif k == 'subscribe_low_all':
                    usages.subscribe_low_all = True
                elif k == 'subscribe_med_all':
                    usages.subscribe_med_all = True
                elif k == 'subscribe_high_all':
                    usages.subscribe_high_all = True
                elif k == 'airplane':
                    usages.airplane = True
                elif k == 'bus':
                    usages.bus = True
                elif k == 'train':
                    usages.train = True
                elif k == 'hotel':
                    usages.hotel = True
                elif k == 'other_accommodation':
                    usages.other_accommodation = True
                elif k == 'tour':
                    usages.tour = True
                elif k == 'subscribe_low_one_month':
                    usages.subscribe_low_one_month = True
                elif k == 'subscribe_med_one_month':
                    usages.subscribe_med_one_month = True
                elif k == 'subscribe_high_one_month':
                    usages.subscribe_high_one_month = True
                elif k == 'subscribe_low_three_month':
                    usages.subscribe_low_three_month = True
                elif k == 'subscribe_med_three_month':
                    usages.subscribe_med_three_month = True
                elif k == 'subscribe_high_three_month':
                    usages.subscribe_high_three_month = True
                elif k == 'subscribe_low_six_month':
                    usages.subscribe_low_six_month = True
                elif k == 'subscribe_med_six_month':
                    usages.subscribe_med_six_month = True
                elif k == 'subscribe_high_six_month':
                    usages.subscribe_high_six_month = True
                elif k == 'subscribe_low_one_year':
                    usages.subscribe_low_one_year = True
                elif k == 'subscribe_med_one_year':
                    usages.subscribe_med_one_year = True
                elif k == 'subscribe_high_one_year':
                    usages.subscribe_high_one_year = True
                usages.save()

        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if models.Reward.objects.filter(pk=kwargs['pk']).exists():
            reward = self.get_object()
            reward.deleted = True
            reward.save()
            return JsonResponse({'detail': f'Reward \'{reward.name}\' has been deleted.'},
                                status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Reward not found.'}, status=status.HTTP_404_NOT_FOUND)


class RewardCategoryListCreateView(ListCreateAPIView):
    queryset = models.RewardCategory.objects.all().exclude(deleted=True)
    serializer_class = serializers.RewardCategorySerializer


class RewardCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.RewardCategory.objects.all().exclude(deleted=True)
    serializer_class = serializers.RewardCategorySerializer
