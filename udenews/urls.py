from django.urls import path,include
from rest_framework import routers
from udenews import views
# from .views import NewsCreate
# from .forms import NewsCreate

router = routers.DefaultRouter()
router.register(r'news_rest', views.NewsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.NewsCreate.as_view() , name='news-create'),
]