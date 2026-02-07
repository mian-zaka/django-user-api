from .serializers import MyuserSerializer
from .models import Myuser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

@api_view(['GET'])
def list_users(request):
    try:
        per_page = int(request.query_params.get('per_page', 10))
        page = int(request.query_params.get('page', 1))
    except (ValueError, TypeError):
        return Response(
            {'error': 'Invalid pagination parameters. per_page and page must be integers.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validate pagination parameters
    if per_page <= 0 or page <= 0:
        return Response(
            {'error': 'per_page and page must be positive integers.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    data = Myuser.objects.all().order_by('id')
    paginator = Paginator(data, per_page)
    total_count = paginator.count
    
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        return Response(
            {'error': f'Page {page} is out of range. Total pages: {paginator.num_pages}'},
            status=status.HTTP_404_NOT_FOUND
        )
    except PageNotAnInteger:
        return Response(
            {'error': 'Page must be an integer.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = MyuserSerializer(page_obj.object_list, many=True)
    
    return Response({
        'users': serializer.data,
        'count': total_count,
        'per_page': per_page,
        'total_pages': paginator.num_pages,
        'current_page': page,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
    })


@api_view(['GET'])
def get_user(request, id):
    try:
        obj = Myuser.objects.get(pk=id)
        serializer = MyuserSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Myuser.DoesNotExist:
        return Response(
            {'error': f'User with id {id} does not exist.'},
            status=status.HTTP_404_NOT_FOUND
        )

@swagger_auto_schema(method='delete',properties={'id':openapi.Schema(type=openapi.TYPE_INTEGER)})
@api_view(['DELETE'])
def deleteUser(request, id):
    try:
        obj = Myuser.objects.get(pk=id)
        obj.delete()
        return Response(
            {'message': f'User with id {id} deleted successfully.'},
            status=status.HTTP_200_OK
        )
    except Myuser.DoesNotExist:
        return Response(
            {'error': f'User with id {id} does not exist.'},
            status=status.HTTP_404_NOT_FOUND
        )

@swagger_auto_schema(methods=['put','patch'],request_body=MyuserSerializer)
@api_view(['PUT', 'PATCH'])
def updateUser(request, id):
    try:
        obj = Myuser.objects.get(pk=id)
        serializer = MyuserSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except Myuser.DoesNotExist:
        return Response(
            {'error': f'User with id {id} does not exist.'},
            status=status.HTTP_404_NOT_FOUND
        )

@swagger_auto_schema(method='post',request_body=MyuserSerializer)
@api_view(['POST'])
def CreateUser(request):
    serializer = MyuserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )