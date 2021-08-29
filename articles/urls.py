from django.urls import path
from .views import ( ArticleListView, 
ArticleDetailView, ArticleCreateView, 
ArticleUpdateView, ArticleDeleteView,)

urlpatterns = [
    path('', ArticleListView.as_view(), name="articles"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name="article_update"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
]

# 1. Create an article detail view
# 2. Create an article create view
# 3. Create an artilce update view
# 4. create an artcle delte view
# 5. cceate urlpatterns to map to all of the views
#  To view an article detail, go to : /articles/<int:pk>/
#  to Create an article, go to : /article/new/
#  To update an article go to : /article/<int:pk>/update
#  To Delete an article go to : /articles/<int:pk>/delete