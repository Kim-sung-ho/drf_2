from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # CBV 는 as_view 를 적어줘야한다.
    path('', views.UserView.as_view()),
]
