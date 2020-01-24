from django.contrib.sitemaps import Sitemap
from .models import Job
from .models import Applicant

class JobSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Job.objects.filter(created_at)

    def lastmod(self, obj):
        return obj.created_at

    # def location(self, item):
    #     return reverse(item)
