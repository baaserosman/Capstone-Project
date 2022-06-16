
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly


# class BlogList(generics.ListAPIView):
#     serializer_class=BlogSerializer
#     queryset = Blog.objects.all()

class BlogCRUD(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer
    
   
class CommentCRUD(ModelViewSet):
    queryset = Blog.objects.all()
    # permission_classes=[IsAuthenticated]    
    serializer_class = CommentSerializer
    


    
