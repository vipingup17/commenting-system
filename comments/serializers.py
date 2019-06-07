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
	"""
	Serializer for creating a new comment
	"""

	class Meta:
		model = Comment
		fields = ['id', 'comment_text', 'user', 'parent']

	def create(self, validated_data):
		# Fetch comment text
		comment_text = validated_data.pop('comment_text')
		
		# Fetch the user
		user = validated_data.pop('user')
		
		# Fetch the parent (if any)
		parent = validated_data.pop('parent')
		
		# Depth is 1 by default
		depth = 1

		# If the comment has a parent (i.e the comment is a reply)
		if parent:
			# Check if the depth of the parent is 1
			# A parent with depth 1 is a reply in itself and therefore, this new reply is assigned the parent of it's parent reply
			if parent.depth == 1:
				# Depth for this reply will be 1 as defined above
				parent = parent.parent

		# If the comment is not a reply, the depth should be 0
		else:
			depth = 0

		# Create the comment object
		comment = Comment.objects.create(user=user, comment_text=comment_text, parent=parent, depth=depth)
		
		# Return the comment
		return comment


class CommentChildSerializer(serializers.ModelSerializer):
	"""
	A serilizer for returning replies of a particular comment
	"""

	class Meta:
		model = Comment
		fields = ['id', 'comment_text', 'user', 'parent']


class GetCommentSerializer(serializers.ModelSerializer):

	"""
	Serializer for returning a comment along with all of it's replies
	"""
	child = CommentChildSerializer(many=True)

	class Meta:
		model = Comment
		fields = ['id', 'comment_text', 'user', 'parent', 'child']