from rest_framework import serializers
from .models import Article


# Normal Serializer

# class ArticalSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()

#     def create(self,validated_data):
#         return Article.objects.create(validated_data)

#     def update(self,intance,validated_data):
#         instance.title = validated_data.get('title',intance.title)
#         instance.author = validated_data.get('title',intance.author)
#         instance.email = validated_data.get('title',intance.email)
#         instance.date = validated_data.get('title',intance.date)

#         instance.save()
#         return instance


# ModelSerializer

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id','title','author','email']
        fields = '__all__'