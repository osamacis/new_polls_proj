from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models.deletion import CASCADE

# ---------------------------------------------------------------

# class Custom_user(AbstractUser):
#     account_choice = (('user','user'),('Author','Author'))
#     account_type = models.CharField(max_length=100, choices=account_choice, default='user')
#     def __str__(self):
#         return self.username
    # class Meta(AbstractUser.Meta):
        # swappable = 'AUTH_USER_MODEL'

class User_post(models.Model):
    # app_user_name = models.ManyToOneField( App_User, on_delete = models.CASCADE)
    app_user_name = models.ForeignKey(User, on_delete=models.CASCADE) # manytoOne
    # app_user_name = models.ManyToManyField( App_User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, db_tablespace=True)
    body = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.app_user_name} - {self.title}'
    
    def get_absolute_url(self):
        return reverse('BookView',args=[str(self.id)])

# ---------------------------------------------------------------------

class  Category(models.Model):
    cat_romance  =  "Romance"
    cat_fantacy  =  "Fantacy"
    cat_thriller=  "Thriller"
    cat_horror  =  "Horror"
    cat_crime  =  "Crime"
    cat_true_story=  "True Story"
    category  =  models.CharField(
        max_length=100,
        choices=(
        (cat_crime, cat_crime),
        (cat_fantacy, cat_fantacy),
        (cat_horror, cat_horror),
        (cat_romance, cat_romance),
        (cat_thriller, cat_thriller),
        (cat_true_story, cat_true_story)
          )
    )
    class  Meta:  #new
        verbose_name_plural  =  "Categories" 
    def  __str__(self):
        return  self.category
    
class  Details(models.Model):
    book_name  =  models.CharField( unique=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    pages = models.IntegerField(default=1)
    is_published = models.CharField(max_length=100)
    #is_published
    class  Meta:   #new
        verbose_name_plural  =  "Details"

    def  __str__(self):
        return  self.book_name


class Book(models.Model):
    auther = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    Category = models.CharField(max_length=100)
    pages = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})