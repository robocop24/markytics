from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Report(models.Model):

    location = models.CharField(max_length=255)
    incident_description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    incident_location = models.TextField()
    initial_severity = models.CharField(max_length=255)
    suspected_cause = models.TextField()
    immediate_actions_taken = models.TextField()
    sub_incident_type = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.reported_by