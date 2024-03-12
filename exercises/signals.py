from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WorkoutEntry

@receiver(post_save, sender=WorkoutEntry)
def update_workout_plan(sender, instance, **kwargs):
    workout_plan = instance.workout_plan
    if workout_plan.workoutentry_set.filter(is_complete=False).exists():
        workout_plan.is_complete = False
    else:
        workout_plan.is_complete = True
    workout_plan.save()