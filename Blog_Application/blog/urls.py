from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, AddCommentView


# using class based view.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cat>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name='like-post'),
]