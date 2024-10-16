from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class Evaluation(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Evaluation for {self.faculty.name} on {self.date}'



