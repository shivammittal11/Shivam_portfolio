from django.contrib import admin

# Register your models here.
from shivam_resume.models import UserData, SkillData, ResumeData, ProjectData, ProjectImages, ProjectTechnology, \
    ContactUs


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile_no', 'heading', 'created', 'modified')

admin.site.register(UserData, UserDataAdmin)


class SkillDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'progress', 'status', 'created', 'modified')

admin.site.register(SkillData, SkillDataAdmin)


class ResumeDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'resume', 'status', 'created', 'modified')

admin.site.register(ResumeData, ResumeDataAdmin)


class ProjectDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'position', 'description', 'status', 'created', 'modified')

admin.site.register(ProjectData, ProjectDataAdmin)


class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'image', 'created', 'modified')

admin.site.register(ProjectImages, ProjectImagesAdmin)


class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'name', 'created', 'modified')

admin.site.register(ProjectTechnology, ProjectTechnologyAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_no', 'message', 'created', 'modified')

admin.site.register(ContactUs, ContactUsAdmin)
