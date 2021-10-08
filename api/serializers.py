from rest_framework import serializers

from shop.models import Company


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'title']
