from django.db import models

# Create your models here.
from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# import awwwardsapp
import awardproject


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=300)
    contact = models.CharField(max_length=100)

    def save_profile(self):
        self.save()
    
    def create_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    category = models.TextField(max_length=50, null=True)
    image = CloudinaryField("image")
    url = models.URLField(null=True)
    location = models.CharField(max_length=50, default="Kenya")
    date = models.DateTimeField(auto_now_add=True, null=True)

    
    @classmethod
    def search_project_name(cls, search_term):
        projects = cls.objects.filter(
        title__icontains=search_term)
        return projects    

    def str(self):
        return self.user.username

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    avarage_rate = models.IntegerField(default=0, blank=True, null=True)

    def _str_(self):
        return self.user.username

    def update_rating(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    def __str__(self):
        return self.project
