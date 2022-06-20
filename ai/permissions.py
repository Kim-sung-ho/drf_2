from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class RegisteredMoreThanThreeDaysUser(BasePermission):
    message = "가입 후 3일 이상 지난 사용자만 사용 가능합니다."

    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and
                    request.user.join_date < (timezone.now() - timedelta(seconds=3)))


class RegisteredMoreThanAWeekUser(BasePermission):

    message = '가입 후 1주일 이상 지난 사용자만 사용 가능합니다.'

    def has_permission(self, request, view):
        return bool(request.user and
                    request.user.join_date < (timezone.now() - timedelta(seconds=7)))
