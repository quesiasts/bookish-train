from django.db import models


class Skills(models.Model):
    typeSkill = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"Skills {self.typeSkill} and {self.description}"

class Person(models.Model):
    full_name = models.CharField(max_length=200, null=False)
    age = models.CharField(max_length=5, null=False)
    phone = models.CharField(max_length=10, null=True)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return f"Person: {self.full_name}, {self.age}, {self.phone}"
