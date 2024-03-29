from rest_framework import generics, permissions

from .serializers import ExerciseSerializer, WorkoutPlanSerializer, WorkoutEntrySerializer
from .models import Exercise, WorkoutPlan, WorkoutEntry
# Create your views here.

class ExerciseListView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = []

class ExerciseDetailView(generics.RetrieveAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = []


# class ExerciseCreateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Exercise.objects.all()
#     serializer_class = ExerciseSerializer
#     permission_classes = [permissions.IsAdminUser]

# class ExerciseUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Exercise.objects.all()
#     serializer_class = ExerciseSerializer
#     permission_classes = [permissions.IsAdminUser]

class WorkoutPlanListView(generics.ListCreateAPIView):
    # queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return WorkoutPlan.objects.filter(user=user)

class WorkoutEntryListView(generics.ListCreateAPIView):
    queryset = WorkoutEntry.objects.all()
    serializer_class = WorkoutEntrySerializer
    permission_classes = [permissions.IsAuthenticated]