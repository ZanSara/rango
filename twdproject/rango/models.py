from django.db import models


# NOTE Django automatically creates the primary key

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
	return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    url = models.URLField()
    viewed = models.IntegerField(default=0)
    def __str__(self):
	return self.title

