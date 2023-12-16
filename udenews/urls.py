from django.urls import path,include
from rest_framework import routers
from udenews import views

router = routers.DefaultRouter()
router.register(r'news_rest', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]