from django import forms
from django.db import models
from django.db.models import fields

from .models import Mentor, Group, Comment, Category, Post
class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ["full_name",  "level", "phone", "address", "salary"]



class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["specification", "block", "time", "language", "name", "mentor", "student_qty", "status"] 


# class StudentCreateForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ["full_name", "birth_date", "specification", "level", "phone", "email", "address", "salary"]      


class comentform(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'body']
# class categoryform(forms.ModelForm):

#     class Meta:
#         model = Category
#         fields = ['title', 'slug']

# class postfr(forms.ModelForm):

#     class Meat:
#         model = Post
#         fields = ['category', 'title', 'slug', 'intro', 'body', 'date_added']

