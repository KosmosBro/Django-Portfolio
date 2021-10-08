from rest_framework.generics import ListAPIView

from .serializers import CompanySerializers
from shop.models import Company


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
