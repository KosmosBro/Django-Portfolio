from django.urls import path, include
from rest_framework import routers

from api import api_views as v

router = routers.DefaultRouter()
router.register(r'company', v.CompanyListAPIView),
router.register(r'product', v.ProductListAPIView),
router.register(r'user', v.UserListAPIView),
router.register(r'cart', v.CartListAPIView),
router.register(r'cart_content', v.CartContentListAPIView),


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
