from django.db import models
from django.conf import settings

# Create your models here.

class LeaveRequest(models.Model):
	sent_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)
		
