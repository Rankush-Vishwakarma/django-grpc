from django.db import models

# user model 
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    validator_Node = models.charField(max_length=100)
    party_Id = models.charField(max_length=100)
    threshold = models.DecimalField(max_digits=5, decimal_places=2)
    current_Balance = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward_points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
class TenantTrafficPurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant_traffic_purchase_history')
    Purchased_Amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class TenantTrafficReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant_traffic_reward')
    reward_points = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
      
    