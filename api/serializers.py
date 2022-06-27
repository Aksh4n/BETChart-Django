from rest_framework import serializers
from transactions.models import CurrentPrice , Pot , GreenMember , RedMember , MemberCount
from users.models import UserBankAccount
from django.contrib.auth.models import User


class CurrentPriceSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = CurrentPrice



class PotSerializer(serializers.Serializer):
    pot = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Pot


class UserBankAccountSerializer(serializers.Serializer):
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        model = UserBankAccount

class GreenMemberSerializer(serializers.Serializer):


    a = serializers.CharField()

    class Meta:
        model = GreenMember
        

class RedMemberSerializer(serializers.Serializer):

    a = serializers.CharField()

    class Meta:
        model = RedMember


class MemberCountSerializer(serializers.Serializer):
    gc = serializers.IntegerField()
    rc = serializers.IntegerField()

    class Meta:
        model = MemberCount





