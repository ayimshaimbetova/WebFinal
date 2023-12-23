from django.urls import path
from .views import ArticleAPIView, ArticleDetail

urlpatterns = [
    path("", ArticleAPIView.as_view(), name="article"),
    path("<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
]


