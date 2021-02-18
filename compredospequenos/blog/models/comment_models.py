# Core Django imports.
from django.db import models
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField

# Blog application imports.
from blog.models.article_models import Article


class Comment(models.Model):
    author = CurrentUserField()
    comment = models.TextField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    publishedAt = models.DateTimeField(auto_now=True)
    flagged = models.BooleanField(default=False)
    reason = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('-createdAt',)

    def __str__(self):
        return f"Comment by {self.author.get_full_name()} on {self.article}"
