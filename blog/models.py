from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    author = models.ForeignKey(to='users.SiteAdmin', on_delete=models.PROTECT, null=True, blank=True)
    category = models.ManyToManyField(to='blog.Category', blank=True)
    tag = models.ForeignKey(to='blog.Tag', on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    view_count = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)
    
    def get_absolute_url(self):
        return reverse("blog:single-blog", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ---> id: {self.id}"