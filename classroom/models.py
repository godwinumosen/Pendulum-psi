from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
# Create your models here.


#third party field
from ckeditor.fields import RichTextField

def user_directory_path(instance, filename):
    #this file will be uploaded to MEDIA_ROOT / the user (id)/ the file
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    icon = models.CharField(max_length=100, verbose_name='Icon', default='skill')
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse('categories', args=(self.slug))
    
    def __str__(self):
        return self.title

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to= user_directory_path)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    syllabus = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_owner')
    enrolled = models.ManyToManyField(User)
    
    def __str__(self) -> str:
        return self.title
    
    
    
    