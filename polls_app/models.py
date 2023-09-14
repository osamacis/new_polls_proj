from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField
# -----------------------------------------------------------------
# proxy model inheritance\

class Custom_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('id')

class Company(models.Model):
    name = models.CharField(max_length=100 )
    city = models.CharField(max_length=100)
    # get_company_data = Custom_manager()
    # def __str__(self):
    #     return self.name

class Proxy_company(Company):
    class Meta:
        proxy = True
        # ordering = ['-id']
    def __str__(self):
        return self.name
    def company_domain(self , name):
        return f'IT {self.name}'

# ---------------------------------------------------------------
# multi table inheritance
class Club(models.Model):
    club_name = models.CharField(max_length=100)
    def __str__(self):
        return self.club_name

class Country(Club):
    country_name = models.CharField(max_length=100)
    def __str__(self):
        return self.country_name
# -------------------------------------------------------------------
# abstract base classes
class Common_info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    mobile = PhoneNumberField(null=False, blank=False, unique=True)
    class Meta:
        abstract = True

class Teacher(Common_info):
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name
    class Meta(Common_info.Meta):
        db_table = 'polls_app_teacher_info'

Stream_choice = [('MATH','MATH'),('BIO','BIO'),('ART','ART'),('COMERCE','COMERCE')]

class Student(Common_info):
    stream = models.CharField(max_length=100 ,choices=Stream_choice)
    def __str__(self):
        return self.name
# ---------------------------------------------------------------------------

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self,pub_dat):
        print('aa',timezone.now())
        print('cc',timezone.now()-datetime.timedelta(days=1))
        print(pub_dat)
        print('bb',datetime.timedelta(days=1))
        if pub_dat <=  timezone.now() - datetime.timedelta(days=1):
            return 'published recently:'
        else:
            return 'Not published recently:'
    def get_absolute_url(self):
        return reverse('polls_app:detail',args=[self.id])

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question
