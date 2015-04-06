from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# NOTE: Django automatically creates the primary key

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
	self.slug = slugify(self.name)
	super(Category, self).save(*args, **kwargs)
	
    def __str__(self):
	return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    url = models.URLField()
    viewed = models.IntegerField(default=0)
    def __str__(self):
	return self.title


class UserProfile(models.Model):
    # The standard User class has the following attributes:
    # username - password - email - first name - surname
    # Here we create a Profile where to store additional info.
    # Better to avoid inheritance here: simply use a 1-to-1 relationship
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    # Picture upload requires PIL
    # pip install pillow
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
	return self.user.username
    
