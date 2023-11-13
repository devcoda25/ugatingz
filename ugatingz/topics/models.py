from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('topic_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

class Views(models.Model):

     view_counts = models.PositiveBigIntegerField(default=0,null=True,blank=True)


     class Meta:
        verbose_name = 'view'
        verbose_name_plural = 'views'




class Comment(models.Model):
  

  text = models.TextField(max_length=500,unique=True,null=True,blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
  
  class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Topic(models.Model):
   
   title = models.CharField(max_length=200,unique=True)
   slug  = models.SlugField(max_length=200, unique=True)
   image = models.ImageField(upload_to='images/', blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   edited_at = models.DateTimeField(auto_now=True)

   content = models.TextField(max_length=20000,null=True)
   link = models.URLField(blank=True, null=True)
   Views = models.ForeignKey(Views,on_delete=models.CASCADE,default=0,null=True,blank=True)
   comments = models.ManyToManyField(Comment, related_name='topics' ,null=True,blank=True)

   category = models.ForeignKey(Category, related_name='topics', on_delete=models.CASCADE,null=True)


   

   class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

   def get_url(self):

      if self.category is not None:
         return reverse('topic_detail', args=[self.category.slug, self.slug])
      else:
      # Provide a default value for category_slug
         return reverse('topic_detail', args=['default_category', self.slug])


   def __str__(self):
        return self.title

    

class Section(models.Model):
   topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='sections')
   title = models.CharField(max_length=200)
   content = models.TextField(max_length=20000)

   image = models.ImageField(upload_to='images/', blank=True, null=True)

   class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'


        
   def __str__(self):
        return self.title

