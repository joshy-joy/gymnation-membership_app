from rest_framework import generics
from .models import MembershipPlans, Member, Trainer, CheckIns, MemberTrainerMapping
from .serializers import (
    MembershipPlansSerializer,
    MemberSerializer,
    TrainerSerializer,
    CheckInsSerializer,
    MemberTrainerMappingSerializer,
)

from rest_framework.response import Response

# Member Views
class CreateMemberView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return create_response("success", "memeber created successfully", status.HTTP_201_CREATED, serializer.data)
        return create_response("status", "Data validation failed", status.HTTP_400_BAD_REQUEST)
    
# CheckIns Views
class CheckInsListCreateView(generics.ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return create_response("success", "checkin successfull", status.HTTP_201_CREATED, serializer.data)
        return create_response("status", "Data validation failed", status.HTTP_400_BAD_REQUEST)


# MembershipPlans Views
class MembershipPlansListCreateView(generics.ListCreateAPIView):
    queryset = MembershipPlans.objects.all()
    serializer_class = MembershipPlansSerializer


# Trainer Views
class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer



def create_response(type, msg, code, data=None):
    if data:
        response = {"status": type, "message": msg, "data":data}
    else:
        response = {"status": type, "message": msg}
    return Response(response, status=code)