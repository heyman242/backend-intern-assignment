from django.db import models


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('Incomplete', 'Incomplete'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
