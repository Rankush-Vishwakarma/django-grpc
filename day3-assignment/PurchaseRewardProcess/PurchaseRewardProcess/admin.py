from django.contrib import admin
from .models import User, Reward, TenantTrafficPurchaseHistory, TenantTrafficReward

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'validator_Node', 'party_Id', 'threshold', 'current_Balance']
    search_fields = ['name', 'email', 'validator_Node', 'party_Id']
    
@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['user', 'reward_points']
    search_fields = ['user']

@admin.register(TenantTrafficPurchaseHistory)
class TenantTrafficPurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'Purchased_Amount']
    search_fields = ['user']

@admin.register(TenantTrafficReward)
class TenantTrafficRewardAdmin(admin.ModelAdmin):
    list_display = ['user', 'reward_points']
    search_fields = ['user']
