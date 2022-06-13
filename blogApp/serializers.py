from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    get_comment_count = Blog.comment_count()
    get_like_count = Blog.like_count()
    get_view_count = Blog.view_count()

    class Meta:
        model = Blog
        fields =(
        "title", 
        "content", 
        "image", 
        "published_date",
        "last_update", 
        "author", 
        "status", 
        "get_view_count", 
        "get_comment_count", 
        "get_like_count"
        )


# class QuestionSerializer(serializers.ModelSerializer):
#     answer = AnswerSerializer(many=True, read_only=True)

#     class Meta:
#         model = Question
#         fields = ("updated", "question_text", "difficulty", "date_created", "quiz", "answer", )


# class QuizSerializer(serializers.ModelSerializer):
#     question = QuestionSerializer(many=True, read_only=True)

#     class Meta:
#         model = Quiz
#         fields = ("quiz_name", "created_date", "category", "question")


# class CategorySerializer(serializers.ModelSerializer):
#     quiz_set = QuizSerializer(many=True, read_only=True)
#     class Meta:
#         model = Category
#         fields = ("name", "quiz_set")