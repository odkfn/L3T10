from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.

class Post(models.Model):
    '''
    This class creates the Post model.

    The Post model is utilised to create blog-style update posts.

    :param str title: The title of the post
    :param str body: The body of the post
    :param DateTime date: The date the post was made

    :returns: The title of the post
    :rtype: str
    
    '''
    # Default behaviour - Django creates primary keys for you
    title = models.CharField(max_length=140)    
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

# Adding the below to try and include video players

class Video(models.Model):
    '''
    This class creates the Video model.

    The Video model is utilised to embed a youtube video on the page.

    :param str title: The title of the video
    :param DateTime added: The date when the video was added
    :param str url: The url of the video

    :returns: The title of the post
    :rtype: str
    
    '''
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True, null=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
