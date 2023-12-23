from django.shortcuts import render
from rest_framework import generics, permissions
from blog.models import Post
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly

class BlogAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
