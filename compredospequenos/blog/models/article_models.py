# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings


# Third party app imports
from taggit_selectize.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

# Blog application imports.
from blog.utils.blog_utils import count_words, read_time
from blog.models.category_models import Category
from django.contrib.sites.models import Site


class Article(models.Model):

    # Article status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    # BLOG MODEL FIELDS
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='articles')
    title = models.CharField(max_length=1500, null=False, blank=False)
    subtitle = models.CharField(max_length=1500, null=True, blank=True)
    slug = models.SlugField(max_length=1500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='articles')
    image = models.ImageField(default='article-default.jpg',
                              upload_to='article_pics')
    image_credit = models.CharField(max_length=1000, null=True, blank=True)
    body = RichTextUploadingField(blank=True)
    tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    publishedAt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    count_words = models.CharField(max_length=50, default=0)
    read_time = models.CharField(max_length=50, default=0)
    deleted = models.BooleanField(default=False)

    sites = models.ManyToManyField(Site, related_name='articles')

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        username = self.author.get_full_name()
        return reverse('article_detail', kwargs={'username': slugify(username), 'slug': self.slug})


