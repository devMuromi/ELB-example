from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("hash/", views.HashView.as_view(), name="hash"),
]
