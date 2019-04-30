from django.db import models
from django.utils import timezone
from map import models as map_models
# Create your models here.


class Post(models.Model):
    mood = models.CharField(max_length=4)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    addr_id = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
