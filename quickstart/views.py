from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from quickstart.models import DRFPost
from quickstart.serializers import UserSerializer, GroupSerializer, DRFPostSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class API_objects(generics.ListCreateAPIView):
	queryset = DRFPost.objects.all()
	serializer_class = DRFPostSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
	queryset = DRFPost.objects.all()
	serializer_class = DRFPostSerializer    

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = DRFPost.objects.all().order_by('-id')
	serializer = DRFPostSerializer(tasks, many=True)
	return Response(serializer.data)    

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = DRFPost.objects.get(id=pk)
	serializer = DRFPostSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = DRFPostSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = DRFPost.objects.get(id=pk)
	serializer = DRFPostSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = DRFPost.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

