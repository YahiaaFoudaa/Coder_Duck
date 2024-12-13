from rest_framework import serializers
from api.models import Blog, Comment, Tag, Category, UserProfile


class TagSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Tag    
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Blog    
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment    
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category    
        fields = '__all__'
        

class UserProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserProfile    
        fields = '__all__'