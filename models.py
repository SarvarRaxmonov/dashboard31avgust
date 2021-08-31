from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import related



# Create your models here.
SPEC_CHOICES = [
    ("FRONTEND", "FRONTEND"),
    ("BACKEND", "BACKEND"),
    ("ANDROID", "ANDROID"),
    ("IOS", "IOS"),
    ("FLUTTER", "FLUTTER"),
    ("REACT-N", "REACT-N"),
    ("DESKTOP", "DESKTOP"),
    ("FULLSTACK", "FULLSTACK"),   


    ("FRONTEND", "FRONTEND"),
    ("BACKEND", "BACKEND"),
    ("ANDROID", "ANDROID"),
    ("IOS", "IOS"),
    ("FLUTTER", "FLUTTER"),
    ("REACT-N", "REACT-N"),
    ("DESKTOP", "DESKTOP"),
    ("FULLSTACK", "FULLSTACK"),   
]

class Mentor(models.Model):
    LEVEL_CHOICES = [
        ("JUNIOR", "JUNIOR"),
        ("MIDDLE", "MIDDLE"),
        ("SENIOR", "SENIOR"),   
    ]
    full_name = models.CharField(max_length=100)

    level = models.CharField(max_length=7, choices=LEVEL_CHOICES, default="JUNIOR")
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name



class Group(models.Model):
    BLOCK_CHOICES =  [
        ("HTML/CSS", "HTML/CSS"),
        ("JS/REACT", "JS/REACT"),
        ("PYTHON/DJANGO", "PYTHON/DJANGO"),
        ("PHP/LARAVEL", "PHP/LARAVEL"),  
        ("KOTLIN/ANDROID", "KOTLIN/ANDROID"),
        ("SWIFT/IOS", "SWIFT/IOS"),
        ("DART/FLUTTER", "DART/FLUTTER"),
        ("JS/REACT-N", "JS/REACT-N"),
        ("C#/DESKTOP", "C#/DESKTOP"),
    ]

    TIME_CHOICES = [
        ("11:00-12:30", "11:00-12:30"),
        ("14:00-15:30", "14:00-15:30"),
        ("16:00-17:30", "16:00-17:30"),
        ("18:00-19:30", "18:00-19:30"),   
    ]
    LANGIAGE_CHOICES = [
        ("UZ", "UZ"),
        ("RU", "RU"),
        ("ENG", "ENG"),   
    ]
    STATUS_CHOICES = [
        ("EMPTY", "EMPTY"),
        ("PART", "PART"),
        ("FULL", "FULL"),   
    ]
    
    specification = models.CharField(max_length=10, choices=SPEC_CHOICES, default="FRONTEND")
    block = models.CharField(max_length=16, choices=BLOCK_CHOICES, default="HTML/CSS")
    time = models.CharField(max_length=12, choices=TIME_CHOICES, default="11:00-12:30")
    language = models.CharField(max_length=4, choices=LANGIAGE_CHOICES, default="UZ")
    name = models.CharField(max_length=50)
    mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, blank=True, null=True)
    student_qty = models.PositiveIntegerField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="EMPTY")

    def __str__(self):
        return self.name



class Student(models.Model):
    PAYMENT_CHOICES = [
        ("UNPAID", "UNPAID"),
        ("PAID", "PAID"),   
    ]
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)
    group = models.ForeignKey(Group, on_delete=SET_NULL, blank=True, null=True)
    payment_status = models.CharField(max_length=7, choices=PAYMENT_CHOICES, default="UNPAID")

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title= models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

        
class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE , null = True,blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
     
    intro = models.TextField(default=1)
    body = models.TextField(default=1)

    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
   
    post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE)                                                                                    
    name = models.CharField(max_length=225)
    body = models.TextField(default=1)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


