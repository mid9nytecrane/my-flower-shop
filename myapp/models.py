from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')


    def __str__(self):
        return self.title 
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()    


class Flowers(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category,null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        verbose_name_plural = "Flowers"

    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flowers, self).save()

    def get_absolute_url(self):
        return reverse("detail-page", args=[str(self.slug)])
    
    