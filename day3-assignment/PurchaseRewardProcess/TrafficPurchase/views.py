from django.shortcuts import render

# Create your views here.
def trafficpurchase(request):
    return render(request, 'TrafficPurchase/traffic_purchase.html', {})