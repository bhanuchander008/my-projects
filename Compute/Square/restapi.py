from rest_framework.decorators import api_view
from rest_framework.response import Response
from Square.models import SquareTest
from django.shortcuts import render
from django.core import serializers
from .serializers import SquareTestSerializer
from django.http import JsonResponse

@api_view(['GET'])
def Test(request):
	return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})
'''
@api_view(['GET'])
def getNumber(request,_Number):
    _Number = _Number.replace('%', ' ')
    stud = SquareTest.objects.filter(Number= _Number)
    if stud:
        serializer = SquareTestSerializer(stud,many=True)
        return Response(serializer.data)

    else:
        return Response({"Message": ' Number NOT FOUND'})

@api_view(['POST'])
def PostNum(request):
    Number = request.data.get("Number", None)
    SquareNumber = request.data.get("SquareNumber", None)
    x= SquareTest.objects.create(Number=Number,
                                     SquareNumber=SquareNumber
                                     )

    return Response({'message': 'x {:d} created'.format(x.id)}, status=301)'''


@api_view(['GET', 'POST'])
def post (request,_Number):

    if request.method == 'GET':
        mul = SquareTest.objects.filter(Number=_Number)
        serializer = SquareTestSerializer(mul, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SquareTestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status= 301)
