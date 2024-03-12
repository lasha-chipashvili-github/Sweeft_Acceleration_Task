from django.db import models


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=256, unique=True)
    exercise_description = models.TextField()
    exercise_instructions = models.TextField()
    exercise_equipment = models.CharField(max_length=256)
    target_muscle = models.CharField(max_length=256)


class WorkoutPlan(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    frequency = models.CharField(max_length=20)
    goals = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutEntry')
    is_complete = models.BooleanField(default=False)



class WorkoutEntry(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    is_complete = models.BooleanField(default=False)



