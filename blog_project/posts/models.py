from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category)
    # ekta post multiple categorir moddhe thakte pare
    # abar ekta categorir moddhe multiple post thakte pare
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    # ekta author r multiple post thakte pare(one to many or many to one) 
    # abar multiple post e ekta outhor thakte pare


    def __str__(self):
        return self.title
