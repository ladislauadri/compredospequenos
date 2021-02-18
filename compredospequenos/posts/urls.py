# Core Django imports.
from django.urls import path

# Blog application imports.
from .views import (
    PostView,
    DetalhesDoPostView
)

# Specifies the app name for name spacing.
app_name = "post"

# article/urls.py
urlpatterns = [

    # ARTICLE URLS #

    # /home/
    path(
        route='',
        view=PostView.as_view(),
        name='home'
    ),
    path(
        route='<pk>',
        view=DetalhesDoPostView.as_view(),
        name='post'
    ),
]
