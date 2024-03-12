from django.db import models

# Create your models here.
# class Muscle(models.Model):
#     muscle_name = models.CharField(max_length=128, unique=True)
#
#     def __str__(self):
#         return self.muscle_name


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=256, unique=True)
    exercise_description = models.TextField()
    exercise_instructions = models.TextField()
    exercise_type = models.CharField(max_length=256)
    exercise_equipment = models.TextField()
    # target_muscle = models.ManyToManyField(Muscle)
    target_muscle = models.CharField(max_length=256)




