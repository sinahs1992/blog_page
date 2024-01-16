from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from blog.models import Post
from django.utils import timezone
from django.urls import reverse
class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        current_time =timezone.now()
        return Post.objects.filter(published_date__lte=current_time, status=True)
    
    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, obj):
        return reverse('blog:single-blog', kwargs={'slug': obj.slug})