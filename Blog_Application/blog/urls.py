from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView


# using class based view.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
]
