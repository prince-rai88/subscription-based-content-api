from django.utils import timezone

def check_subscription_status(user):
    if user.subscription_type == "premium" and user.subscription_expiry:
        if user.subscription_expiry < timezone.now():
            user.subscription_type = "free"
            user.subscription_expiry = None
            user.save()