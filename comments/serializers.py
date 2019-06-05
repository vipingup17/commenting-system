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

# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['username']
# 		extra_kwargs = {
#             'username': {
#                 'validators': [UnicodeUsernameValidator()],
#             }
#         }

class CommentSerializer(serializers.ModelSerializer):
	# user = UserSerializer(read_only=True)

	class Meta:
		model = Comment
		fields = ['comment_text', 'user', 'parent']

	def create(self, validated_data):
		comment_text = validated_data.pop('comment_text')
		user = validated_data.pop('user')
		parent = validated_data.get('parent')
		comment = Comment.objects.create(user=user, comment_text=comment_text, parent=parent)
		return comment


