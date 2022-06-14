from django.shortcuts import render
from rest_framework import generics
from blogApp.models import Blog
from blogApp.serializers import BlogSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly

# class BlogList(generics.ListAPIView):
#     serializer_class=BlogSerializer
#     queryset = Blog.objects.all()

class BlogCRUD(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer
    
   

    
