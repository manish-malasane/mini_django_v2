from django.db import models


class StudentInfo(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=250)
    skill_set = models.CharField(max_length=500)

    def __str__(self):
        return self.name
