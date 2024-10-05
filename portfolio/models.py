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
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='portfolios')
    features = models.ManyToManyField(Features, related_name='portfolios')
    image = models.CharField(max_length=255)
    live_link_frontend = models.CharField(max_length=255, null=True, blank=True)
    live_link_backend = models.CharField(max_length=255, null=True, blank=True)
    github_link_frontend = models.CharField(max_length=255, blank=True, null=True)
    github_link_backend = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
