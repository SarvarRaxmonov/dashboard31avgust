from django.contrib import admin
from .models import Mentor, Group, Comment, Category, Post

# Register your models here.

admin.site.register(Mentor)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Post)
