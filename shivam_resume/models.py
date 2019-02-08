from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" %(self.user.first_name)


class SkillData(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    progress = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)


class ResumeData(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    resume = models.FileField(upload_to='docs/', null=False, blank=False)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.title)


class ProjectData(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    cover_image = models.ImageField(upload_to='project_images/', null=False, blank=False)
    position = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)


class ProjectImages(models.Model):
    project = models.ForeignKey(ProjectData, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.project.name)


class ProjectTechnology(models.Model):
    project = models.ForeignKey(ProjectData, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.project.name)


class ContactUs(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)