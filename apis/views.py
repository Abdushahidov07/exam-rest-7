from rest_framework.generics import *
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filtres import *
from .serializers import *
from .models import *


# User apis Crud and functionaly
class UserListAPIView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username',"f_name","l_name",]
    search_fields = ['username']

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class UserCreateAPIView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class UserDeleteAPIView(DestroyAPIView):
    queryset = Users.objects.all()



# Group apis Crud and functionaly
class GroupListAPIView(ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers

class GroupRetrieveAPIView(RetrieveAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers


class GroupCreateAPIView(CreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers


class GroupRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers


class GroupDeleteAPIView(DestroyAPIView):
    queryset = Groups.objects.all()




# Attenden apis Crud and functionaly
class AttendenListAPIView(ListAPIView):
    queryset = Attendens.objects.all()
    serializer_class = AttendensSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['user',"omad","raft","attended_time","missed_time","timeout_time"] 
    search_fields = ['prichina']


class AttendenRetrieveAPIView(RetrieveAPIView):
    queryset = Attendens.objects.all()
    serializer_class = AttendensSerializers


class AttendenCreateAPIView(CreateAPIView):
    queryset = Attendens.objects.all()
    serializer_class = AttendensSerializers


class AttendenRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Attendens.objects.all()
    serializer_class = AttendensSerializers


class AttendenDeleteAPIView(DestroyAPIView):
    queryset = Attendens.objects.all()