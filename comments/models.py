# -*- coding: utf-8 -*-
#
# authors: Vipin
#
# Created on Tue June 4 2019


# -- Internal Libraries
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
	"""
	Comment model to store comments submitted by the users
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_text = models.TextField()
	parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="child", null=True, blank=True)
	depth = models.IntegerField(default=0)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		# Returning first 100 characters of every comment text
		return self.comment_text[:100] + ' (' + str(self.pk) + ')'

	def has_permission(self, user_id):
		if self.user.id == user_id:
			return True
		return False