from rest_framework import serializers
from club import models


class TopFiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopFiveUsers
        fields = "__all__"


class RewardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RewardCategory
        fields = ("id", "name", "icon")


class RewardUsageGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RewardUsageGuide
        fields = ("id", "guide")


class RewardRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RewardRule
        fields = ("id", "rule")


class RewardUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RewardUsage
        fields = ("id", "all", "all_transport", "accommodation_all", "tour_all", "subscribe_low_all",
                  "subscribe_med_all", "subscribe_high_all", "airplane", "bus", "train", "hotel", "other_accommodation",
                  "tour", "subscribe_low_one_month", "subscribe_med_one_month", "subscribe_high_one_month",
                  "subscribe_low_three_month", "subscribe_med_three_month", "subscribe_high_three_month",
                  "subscribe_low_six_month", "subscribe_med_six_month", "subscribe_high_six_month",
                  "subscribe_low_one_year", "subscribe_med_one_year", "subscribe_high_one_year")


class RewardListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.name')
    usages = RewardUsageSerializer(source="cru_reward", read_only=True)
    rule = RewardRuleSerializer(read_only=True, source='crr_reward', many=False)
    # category = serializers.SerializerMethodField()
    #
    # def get_category(self, obj):
    #     return RewardCategorySerializer(instance=obj.category).data

    class Meta:
        model = models.Reward
        fields = ("id", "name", "type", 'desc_title', 'rule', "category", "amount", "max_amount", "required_point",
                  "avatar", "date_validate", "icon", 'get_type', 'usage_validate_per_user', 'usage_validate_total',
                  'usages', 'category_id')


class RewardSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.name')
    guides = RewardUsageGuideSerializer(read_only=True, source='crug_reward')
    rules = RewardRuleSerializer(read_only=True, source='crr_reward')
    usages = RewardUsageSerializer(read_only=True, source='cru_reward',)

    # def get_category(self, obj):
    #     return RewardCategorySerializer(instance=obj.category).data

    class Meta:
        model = models.Reward
        fields = ("id", "name", "type", "category", "guides", "rules", "usages", "amount", "max_amount", "avatar",
                  "required_point", "desc_title", "desc", "date_validate", "icon", 'description',
                  'usage_validate_per_user', 'usage_validate_total', 'category_id', 'get_type')

