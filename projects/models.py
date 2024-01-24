from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ('EN_ATTENTE', 'En Attente'),
        ('EN_COURS', 'En Cours'),
        ('SUSPENDU', 'Suspendu'),
        ('TERMINE', 'Terminé'),
        ('EN_EVAL', 'En Évaluation'),
    ]

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EN_ATTENTE')

    def __str__(self):
        return self.name


class Tache(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    number_order = models.IntegerField()
    description = models.TextField()
    delay = models.DateField()
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number_order} - {self.description}"
