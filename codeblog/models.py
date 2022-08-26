from django.db import models
from ckeditor.fields import RichTextFiel

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.name

class Post(models.Model):
	genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True )	
	title = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField()
	primary = 'primary'
	secondary = 'secondary'
	success = 'success'
	danger = 'danger'
	warning = 'warning'
	info = 'info'
	dark = 'dark'
	IMPORTANCE_CHOICES = [
        (primary, 'important'),
        (secondary, 'not important'),
        (success, 'very important'),
        (danger, 'urgent'),
        (warning, 'temporary'),
        (info, 'moderate'),
        (dark, 'least important'),
    ]
	importance = models.CharField(max_length=100, null=False, blank=False, 
		choices=IMPORTANCE_CHOICES, default=info)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    heading = models.CharField(max_length=100, null=False, blank=False)
    code = RichTextField(blank=False, null=False)

    def __str__(self):
    	return self.heading

