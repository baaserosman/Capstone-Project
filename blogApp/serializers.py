from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    # get_comment_count = serializers.ReadOnlyField(source="comment_count")
    # get_like_count = serializers.ReadOnlyField(source="like_count")
    # get_view_count = serializers.ReadOnlyField(source="view_count")

    class Meta:
        model = Blog
        fields = (
        "title", 
        "content", 
        "image", 
        "publish_date",
        "last_update", 
        "author", 
        "status",
        "comment_count", 
        "view_count",         
        "like_count",
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