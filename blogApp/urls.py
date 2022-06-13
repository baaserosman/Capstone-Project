from django.urls import path, include
from blogApp.views import BlogList

urlpatterns = [    
   path('blog/', BlogList.as_view()),

]
