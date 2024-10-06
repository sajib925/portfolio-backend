from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Features(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description_1 = models.TextField(null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='portfolios')
    features = models.ManyToManyField(Features, related_name='portfolios')
    image_1 = models.CharField(max_length=255)
    image_2 = models.CharField(max_length=255, null=True, blank=True)
    image_3 = models.CharField(max_length=255, null=True, blank=True)
    live_link_frontend = models.CharField(max_length=255, null=True, blank=True)
    live_link_backend = models.CharField(max_length=255, null=True, blank=True)
    github_link_frontend = models.CharField(max_length=255, blank=True, null=True)
    github_link_backend = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
