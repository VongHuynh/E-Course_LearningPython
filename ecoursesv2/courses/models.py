from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# model user


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')

# model category


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):  # override toString method
        return self.name

# model base


class MyModelBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

# Model Course


class Course(MyModelBase):  # course_course
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ['-id']

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)


class Lesson(MyModelBase):  # course_lesson
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    course = models.ForeignKey(Course,
                               related_name="lessons",
                               on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        'Tag', related_name="lessonTag", blank=True, null=True)



class Comment(models.Model):
    content = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class ActionBase(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)


class LessonView(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)