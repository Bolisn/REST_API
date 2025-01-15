from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField

    def __str__(self):
        return self.name

class job_post(models.Model):
        # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title