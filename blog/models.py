from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "images/")


    def __str__(self):
        return self.title

    def summery(self):
        if len(self.body) > 300 :
            return self.body[:300]+"....."
        else:
            return self.body
