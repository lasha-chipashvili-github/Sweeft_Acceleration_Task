from django.db import models
from django.contrib.auth.models import AbstractUser
from exercises.models import Exercise


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=320, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class UserWeigth(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    currnet_weight = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date")

    def __str__(self):
        return f"{self.user.username}'s Weight on {self.date}"


class CustomUserInfo(models.Model):
    class Sex(models.IntegerChoices):
        Male = 1
        Female = 0

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sex = models.IntegerField(choices=tuple(map(lambda x: (int(x[0]), x[1]), Sex.choices)),
                                       default=Sex.Male, verbose_name="user's sex")
    height = models.DecimalField(max_digits=3, decimal_places=2)
    bmi = models.FloatField(blank=True, null=True)
    classification = models.CharField(blank=True, null=True)


    def calculate_bmi(self):
        """
        Calculate Body Mass Index (BMI) and classify it using metric units.

        Returns:
            tuple: A tuple containing the calculated BMI and its classification.
        """

        self.latest_weight = self.userweight_set.order_by('-date').first()
        self.weight_kg = self.latest_weight.current_weight
        self.bmi = self.weight_kg / (self.height_m ** 2)
        self.classification = None

        if self.bmi < 18.5:
            self.classification = 'Underweight'
        elif 18.5 <= self.bmi < 24.9:
            self.classification = 'Normal weight'
        elif 25 <= self.bmi < 29.9:
            self.classification = 'Overweight'
        else:
            self.classification = 'Obesity'

        return self.bmi, self.classification


    def save(self):
        self.bmi, self.classification = self.calculate_bmi()
        super(CustomUserInfo, self).save()


