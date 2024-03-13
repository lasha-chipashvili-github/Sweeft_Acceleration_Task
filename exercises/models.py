from django.db import models


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=256, unique=True)
    exercise_description = models.TextField()
    exercise_instructions = models.TextField()
    exercise_equipment = models.CharField(max_length=256)
    target_muscle = models.CharField(max_length=256)


class WorkoutPlan(models.Model):
    class BMIClassification(models.IntegerChoices):
        UNDERWEIGHT = 1, "Underweight"
        NORMALWEIGHT = 2, "Normal weight"
        OVERWEIGHT = 3, "Overweight"
        OBESITY = 4, "Obesity"

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    goals = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutEntry')
    is_complete = models.BooleanField(default=False)
    bmi_goal = models.IntegerField(choices=BMIClassification.choices, null=True, blank=True)
    bmi_goal_is_acheived = models.BooleanField(default=False)

    def is_bmi_goal_acheived(self):
        from accounts.models import CustomUserInfo
        user_current_bmi = CustomUserInfo.objects.filter(user=self.user).first().bmi
        if self.bmi_goal == user_current_bmi:
            return True
        return False



    def save(self):
        self.bmi_goal_is_acheived = self.is_bmi_goal_acheived()
        super(WorkoutPlan, self).save()

class WorkoutEntry(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions_per_week = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)
    distance_km = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    is_complete = models.BooleanField(default=False)



