from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField("title of post", max_length = 100)
    content = models.TextField("content of post")
    thumbnail = models.ImageField("Thumbnail image", upload_to = "post", blank = True)


    '''
    __str__이 필요한 이유:
    만약 __str__이 없다면 db에서 확인할때, Post object(1)과 같은 형태로 나타나게됨.
    '''
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField("content of comment")

    def __str__(self):
        return f"{self.post.title}'s comment (ID : {self.id})"
