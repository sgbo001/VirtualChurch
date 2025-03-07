from django.db import models
from django.contrib.auth.models import User


class LiveStream(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stream_url = models.URLField(help_text="YouTube Live URL")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class VideoLibrary(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(help_text="YouTube or Azure Video URL")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - ${self.amount}"

# Community Resources (Bible Study, Events, Forums)
class CommunityResource(models.Model):
    RESOURCE_TYPES = (
        ('bible_study', 'Bible Study'),
        ('event', 'Event'),
        ('forum', 'Forum Discussion'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    resource_type = models.CharField(max_length=15, choices=RESOURCE_TYPES)
    files = models.FileField(upload_to='learning_files', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_resource_type_display()}: {self.title}"

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.date}"

