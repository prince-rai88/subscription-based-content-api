from django.urls import path
from .views import AccessLogListView, MonthlyUsageReportView, PremiumContentView, RegisterView, UpgradeSubscriptionView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('premium-content/', PremiumContentView.as_view(), name='premium-content'),
    path("upgrade-premium/", UpgradeSubscriptionView.as_view(), name="upgrade-premium"),
    path("admin/access-logs/", AccessLogListView.as_view(), name="access-logs"),
    path("admin/monthly-report/", MonthlyUsageReportView.as_view()),
]