from articles import views
from .views import ArticleListView, ArticleDetailView, CreatePostView, ArticleUpdate, ArticleDelete, ArticleAboutView
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('create/<int:pk>/', ArticleUpdate.as_view(), name='article_edit'),
    path('delete/<int:pk>/', ArticleDelete.as_view(), name='delete'),  
    path('about/', ArticleAboutView.as_view(), name='about'),  
    
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('test', views.test, name='test'),
    path('logout', views.logout, name='logout'),
]
