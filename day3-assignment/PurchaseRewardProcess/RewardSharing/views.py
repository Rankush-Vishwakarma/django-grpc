from django.shortcuts import render

# Create your views here.

def rewardsharing(request):
    return render(request, 'RewardSharing/reward_sharing.html', {})