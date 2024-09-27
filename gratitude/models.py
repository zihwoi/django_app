from django.db import models
from django.utils import timezone

class GratitudeEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Gratitude Entries"  # This will display properly in the admin panel
