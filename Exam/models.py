from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Name = models.CharField(max_length=200)
    Exam_Code = models.CharField(max_length=200)
    Created_Date = models.DateTimeField(default=timezone.now)
    Subject = models.TextField()
    Duration = models.FloatField()
    # d1 = datetime.timedelta(days =-1, seconds = 68400
    # geek_object =Post.objects.create(Duration = d1) 
    # geek_object.save();
    published_date = models.DateTimeField(blank=True, null=True)
    Created_By = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # def dur():
    #     d = datetime.timedelta(days =-1, seconds = 68400) 
    #     self.Duration=d
    #     self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name
