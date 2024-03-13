from rest_framework import serializers

from exercises.models import Exercise, WorkoutPlan, WorkoutEntry


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["exercise_name", "exercise_description", "exercise_instructions", "exercise_equipment", "target_muscle"]

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = "__all__"

class WorkoutEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutEntry
        fields = "__all__"

