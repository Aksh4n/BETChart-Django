from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from transactions.models import CurrentPrice , Pot , GreenMember , RedMember , MemberCount
from .serializers import CurrentPriceSerializer , PotSerializer , UserBankAccountSerializer , GreenMemberSerializer , RedMemberSerializer , MemberCountSerializer
from users.models import UserBankAccount



@api_view(['GET'])
def getData(request):

    currentprice = CurrentPrice.objects.get(id=1)
    serializer = CurrentPriceSerializer(currentprice)

    return Response(serializer.data)




@api_view(['GET'])
def potData(request):

    pot = Pot.objects.get(id=1)
    serializer = PotSerializer(pot)

    return Response(serializer.data)



@api_view(['GET'])
def ballanceData(request):


    


    balance = UserBankAccount.objects.get(id=request.user.account.id)
    serializer = UserBankAccountSerializer(balance)

    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = CurrentPriceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    



@api_view(['GET'])
def gmemberData(request):

    a = GreenMember.objects.all()
    serializer = GreenMemberSerializer(a , many=True)

    return Response(serializer.data)



@api_view(['GET'])
def rmemberData(request):

    a = RedMember.objects.all()
    serializer = RedMemberSerializer(a , many=True)

    return Response(serializer.data)


@api_view(['GET'])
def countData(request):

    a = MemberCount.objects.get(id=1)


    serializer = MemberCountSerializer(a)

    return Response(serializer.data)
