from django.urls import path
from .views import HomeView, ArticleDetailView


# using class based view.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<pk>', ArticleDetailView.as_view(), name='article-detail'),
]
