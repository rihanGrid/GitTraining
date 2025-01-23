from django.db import models

# Create your models here.

class Students(models.Model):
    GENDER_CHOICES = [
        ('Male', 'M'),
        ('Female', 'F')
    ]
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    student_class = models.CharField(max_length=50)
    major_Subject = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    