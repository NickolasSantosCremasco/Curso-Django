from django.db import models

# the class is like one table in databases
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')




