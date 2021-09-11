from django.urls import path
import shop.views as v

urlpatterns = [
    path('', v.view_home, name='home'),
    path('register/', v.view_register, name='register'),
    path('log_in/', v.view_login, name='login'),
    path('log_out/', v.view_log_out, name='logout'),
    path('product/', v.view_product, name='product'),

]
