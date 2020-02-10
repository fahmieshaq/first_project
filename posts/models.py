from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) # set once during record creation
    date_modified = models.DateTimeField(auto_now=True) # auto_now will update every time you save the model.

    def __str__(self):
        return self.title
