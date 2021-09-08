from django.urls import path
import shop.views as v

urlpatterns = [
    path('', v.view_home, name='home'),
    path('log_in/', v.view_login, name='login'),
]
