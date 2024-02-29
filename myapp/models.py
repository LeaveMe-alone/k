from django.db import models
from django.utils.text import slugify
from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)  # Make sure blank is allowed
    intro = models.TextField()
    paragraph_1 = models.TextField()
    my_back_quote = models.TextField()
    subheading = models.TextField()
    paragraph_2 = models.TextField()
    paragraph_3 = models.TextField()
    conclusion = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate slug only if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
