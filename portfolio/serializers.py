from rest_framework import serializers
from .models import Portfolio, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PortfolioSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'tags', 'image', 'live_link', 'github_link_frontend', 'github_link_backend']  # Include new fields

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        portfolio = Portfolio.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            portfolio.tags.add(tag)
        return portfolio

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.live_link = validated_data.get('live_link', instance.live_link)  # Handle live_link
        instance.github_link_frontend = validated_data.get('github_link_frontend', instance.github_link_frontend)  # Handle github_link_frontend
        instance.github_link_backend = validated_data.get('github_link_backend', instance.github_link_backend)  # Handle github_link_backend
        instance.save()

        if tags_data:
            # Clear existing tags and add the updated tags
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)

        return instance
