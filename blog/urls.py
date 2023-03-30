from django.urls import path
from blog.views import BlogListView, BlogDetailView, category_list

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path ('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    path ('blog/category/<int:id>/', category_list, name='category_blogs'),
    # path ('blog/<int:pk>/', CommentView.as_view(), name='comment')

]