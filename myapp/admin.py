from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class EnjoyInline(admin.StackedInline):
  model = Enjoy
  extra = 0
  
class CommentInline(admin.StackedInline):
  model = Comment
  extra = 0
  
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  inlines = [CommentInline]
  
class SectionAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}

class SectionInline(admin.StackedInline):
  model = Section
  extra = 0
  
class TopicAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  inlines = [SectionInline]

  
admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)


class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False
  
class CustomUserAdmin(UserAdmin):
  inlines = (ProfileInline, EnjoyInline,)
  
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



# class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
#   fieldsets = UserAdmin.fieldsets
  
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)



# from django.contrib import admin
# from .models import Post, Topic, Profile, Enjoy, Section, Comment
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from import_export.admin import ImportExportModelAdmin


  
# class SectionAdmin(ImportExportModelAdmin):
#   fields = ['id', 'title', 'topic', 'slug']

# class TopicAdmin(ImportExportModelAdmin):
#   fields = ['id', 'title', 'slug']


# admin.site.register(Topic, TopicAdmin)
# admin.site.register(Section, SectionAdmin)
  