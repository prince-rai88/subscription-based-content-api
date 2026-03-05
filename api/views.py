from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegistrationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from datetime import timedelta
from django.utils import timezone

from rest_framework.generics import ListAPIView
from .serializers import PremiumAccessLogSerializer


from .models import PremiumAccessLog




import csv
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from django.utils.timezone import make_aware
from datetime import datetime



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class PremiumContentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

    def get(self, request):

        # # Check if subscription expired
        # check_subscription_status(request.user)

        if request.user.subscription_type != "premium":
            return Response(
                {"detail": "Premium subscription required to view this content."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Log premium access
        PremiumAccessLog.objects.create(
            user=request.user,
            endpoint=request.path,
            method=request.method,
            ip_address=self.get_client_ip(request)
        )

        return Response(
            {"detail": "Welcome to the premium content!"},
            status=status.HTTP_200_OK
        )
    
    
class UpgradeSubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        now = timezone.now()

        # Case 1: User already premium
        if user.subscription_type == 'premium' and user.subscription_expiry:

            # If subscription still active
            if user.subscription_expiry > now:
                new_expiry = user.subscription_expiry + timedelta(days=30)
            else:
                # Expired premium
                new_expiry = now + timedelta(days=30)

        else:
            # Free user
            new_expiry = now + timedelta(days=30)

        user.subscription_type = 'premium'
        user.subscription_expiry = new_expiry
        user.save()

        return Response(
            {
                "detail": "Subscription upgraded successfully.",
                "subscription_expiry": user.subscription_expiry
            },
            status=status.HTTP_200_OK
        )
    


class AccessLogListView(ListAPIView):
    queryset = PremiumAccessLog.objects.all().order_by("-timestamp")
    serializer_class = PremiumAccessLogSerializer
    permission_classes = [IsAdminUser]



class MonthlyUsageReportView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        year = int(request.query_params.get("year"))
        month = int(request.query_params.get("month"))

        start_date = make_aware(datetime(year, month, 1))

        if month == 12:
            end_date = make_aware(datetime(year + 1, 1, 1))
        else:
            end_date = make_aware(datetime(year, month + 1, 1))

        logs = PremiumAccessLog.objects.filter(
            timestamp__gte=start_date,
            timestamp__lt=end_date
        )

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=monthly_report.csv"

        writer = csv.writer(response)
        writer.writerow(["User", "Endpoint", "Method", "IP Address", "Timestamp"])

        for log in logs:
            writer.writerow([
                log.user.email,
                log.endpoint,
                log.method,
                log.ip_address,
                log.timestamp
            ])

        return response