from django.db import models
from author.models import Author
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=107)
    about = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE,default=None)
    # ekjon author r ekta mato profile thakbe
    def __str__(self):
        return self.name
    
   
