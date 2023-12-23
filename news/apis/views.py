from django.shortcuts import render
from rest_framework import generics, permissions
from articles.models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly

class ArticleAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer