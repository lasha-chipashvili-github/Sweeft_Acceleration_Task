from django.contrib import admin

from .models import Exercise, WorkoutPlan, WorkoutEntry

# Register your models here.
class ExerciseAdmin(admin.ModelAdmin):
    fields = ('exercise_name', 'exercise_description', 'exercise_instructions', 'exercise_equipment', 'target_muscle')
    list_display = ('exercise_name', 'exercise_equipment', 'target_muscle')

admin.site.register(Exercise, ExerciseAdmin)


class WorkoutPlanAdmin(admin.ModelAdmin):
    fields = ('user', 'frequency', 'goals',  'is_complete')

admin.site.register(WorkoutPlan, WorkoutPlanAdmin)


class WorkoutEntryAdmin(admin.ModelAdmin):
    fields = ('workout_plan', 'exercise', 'repetitions', 'duration_minutes', 'distance_km', 'is_complete')

admin.site.register(WorkoutEntry, WorkoutEntryAdmin)