
from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('category/<slug:category_slug>/',views.post_by_category,name="posts_by_category"),
    path('search/',views.blogs,name="search_blogs"),
    path("single-blog/<slug:slug>",views.singleBlog,name="singleBlog")
]
