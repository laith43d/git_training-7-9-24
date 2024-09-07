from django.db import models


class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    trainings = models.ManyToManyField(Training, related_name='instructors')

    def __str__(self):
        return self.name

class InstructorTraining(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.instructor.name + ' - ' + self.training.name