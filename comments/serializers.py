# -*- coding: utf-8 -*-
#
# authors: Vipin
#
# Created on Tue June 5 2019

# -- Internal Libraries
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import Comment

# -- External Libraries
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = ['comment_text', 'user', 'parent']

	def create(self, validated_data):
		comment_text = validated_data.pop('comment_text')
		user = validated_data.pop('user')
		parent = validated_data.get('parent')
		depth = 1
		if parent:
			if parent.depth == 1:
				parent = parent.parent
		else:
			depth = 0
		comment = Comment.objects.create(user=user, comment_text=comment_text, parent=parent, depth=depth)
		return comment


class GetCommentSerializer(serializers.ModelSerializer):
	replies = serializers.SerializerMethodField()

	class Meta:
		model = Comment
		fields = ['comment_text', 'user', 'parent', 'replies']

	def get_replies(self, obj): 
		return {  child.comment_text for child in obj.child.all().order_by('created_date') }


