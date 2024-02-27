from django.db import models
from django.utils.text import slugify
from datetime import datetime


class Post(models.Model):
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
    image = models.ImageField(upload_to='uploads/', blank=True,null=True)
    image_2 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        # Generate slug only if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
