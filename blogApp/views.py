from django.shortcuts import render
from rest_framework import generics
from blogApp.models import Blog
from blogApp.serializers import BlogSerializer

class BlogList(generics.ListAPIView):
    serializer_class=BlogSerializer
    queryset = Blog.objects.all()
    
