from django.db import models
from django.contrib.auth.models import AbstractUser
from exercises.models import Exercise


# Create your models here.
class CustomUser(AbstractUser):
    class Sex(models.IntegerChoices):
        Male = 1
        Female = 0

    email = models.EmailField(max_length=320, unique=True)
    sex = models.IntegerField(choices=tuple(map(lambda x: (int(x[0]), x[1]), Sex.choices)),
                                       default=Sex.Male, verbose_name="user's sex")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']




class CustomUserInfo(models.Model):
    class BMIClassification(models.IntegerChoices):
        UNDERWEIGHT = 1, "Underweight"
        NORMALWEIGHT = 2, "Normal weight"
        OVERWEIGHT = 3, "Overweight"
        OBESITY = 4, "Obesity"


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    height = models.DecimalField(max_digits=3, decimal_places=2)
    current_weight = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField(auto_now=True)
    bmi = models.FloatField(blank=True, null=True)
    classification = models.IntegerField(choices=BMIClassification.choices, null=True, blank=True)


    def calculate_bmi(self, weight, height):
        """
        Calculate Body Mass Index (BMI) and classify it using metric units.

        Returns:
            tuple: A tuple containing the calculated BMI and its classification.
        """

        self.bmi = weight / (height ** 2)
        self.classification = None

        if self.bmi < 18.5:
            self.classification = 1 # 'Underweight'
        elif 18.5 <= self.bmi < 24.9:
            self.classification = 2 # 'Normal weight'
        elif 25 <= self.bmi < 29.9:
            self.classification = 3 # 'Overweight'
        else:
            self.classification = 4 # 'Obesity'

        return self.bmi, self.classification


    def save(self):
        self.bmi, self.classification = self.calculate_bmi(self.current_weight, self.height)
        super(CustomUserInfo, self).save()


