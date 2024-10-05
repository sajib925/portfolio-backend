from rest_framework import serializers
from .models import Portfolio, Tag, Features

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['id', 'name']

class PortfolioSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    features = FeaturesSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = [
            'id',
            'title',
            'description',
            'tags',
            'features',
            'image',
            'live_link_frontend',
            'live_link_backend',
            'github_link_frontend',
            'github_link_backend'
        ]

    def create(self, validated_data):
        # Extract tags and features data
        tags_data = validated_data.pop('tags')
        features_data = validated_data.pop('features')

        # Create the Portfolio instance
        portfolio = Portfolio.objects.create(**validated_data)

        # Handle tags
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            portfolio.tags.add(tag)

        # Handle features
        for feature_data in features_data:
            feature, created = Features.objects.get_or_create(name=feature_data['name'])
            portfolio.features.add(feature)

        return portfolio

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        features_data = validated_data.pop('features', None)

        # Update basic fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.live_link_frontend = validated_data.get('live_link_frontend', instance.live_link_frontend)
        instance.live_link_backend = validated_data.get('live_link_backend', instance.live_link_backend)
        instance.github_link_frontend = validated_data.get('github_link_frontend', instance.github_link_frontend)
        instance.github_link_backend = validated_data.get('github_link_backend', instance.github_link_backend)
        instance.save()

        # Update tags if provided
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)

        # Update features if provided
        if features_data:
            instance.features.clear()
            for feature_data in features_data:
                feature, created = Features.objects.get_or_create(name=feature_data['name'])
                instance.features.add(feature)

        return instance
