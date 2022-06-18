from django.urls import path, include
from blogApp.views import BlogCRUD, CommentCRUD

from rest_framework import routers

router = routers.DefaultRouter()
router.register('blogs', BlogCRUD)
router.register('comments', CommentCRUD)


urlpatterns = [    
   # path('blog/', BlogList.as_view()),
   path('', include(router.urls)),
]
