from django.urls import path

from .views import (ExerciseListView, ExerciseDetailView,
                    # ExerciseCreateView, ExerciseUpdateView,
                    WorkoutEntryListView, WorkoutPlanListView)

urlpatterns = [
    path('', ExerciseListView.as_view(), name='exercise-list'),
    path('<int:pk>/', ExerciseDetailView.as_view(), name='exercise'),
    # path('<int:pk>/', ExerciseUpdateView.as_view(), name='exercise-update'),
    # path('create/', ExerciseCreateView.as_view(), name='exercise-create'),
    path('workoutplans/', WorkoutPlanListView.as_view(), name='workout-list'),
    path('workoutentries/', WorkoutEntryListView.as_view(), name='workout-list'),
]