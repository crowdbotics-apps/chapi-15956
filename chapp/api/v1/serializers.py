from rest_framework import serializers
from chapp.models import CHdb


class CHdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHdb
        fields = "__all__"
