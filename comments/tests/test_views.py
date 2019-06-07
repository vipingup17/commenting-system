# -*- coding: utf-8 -*-
#
# authors: Vipin
#
# Created on Fri June 7 2019

# -- External Libraries
from django.test import TestCase
from django.contrib.auth.models import User

# -- Local Libraries
from comments.models import Comment

class CommentCreateViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		user = User.objects.create(username='testuser')
		user.set_password('testpass')
		user.save()

	def test_response_status_on_post_data(self):
		post_data = {
			"comment_text": "This is comment 1",
			"user": 1,
			"parent": None
		}
		response = self.client.post('/comments/create', data=post_data, content_type='application/json')
		self.assertEqual(response.status_code, 201)


class CommentDetailViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		user_two = User.objects.create(username='testuser')
		user_two.set_password('testpass')
		user_two.save()

		# Crating another user
		user_three = User.objects.create(username='anotheruser')
		user_three.set_password('testpass')
		user_three.save()

		# Creating a comment to test GET operation
		comment = Comment.objects.create(comment_text="This is a test comment", user=user_two)
		comment.save()

	def test_response_status_on_get_request(self):
		response = self.client.get('/comments/2')
		self.assertEqual(response.status_code, 200)

	def test_response_data_received_on_get_request(self):
		response = self.client.get('/comments/2')
		data = {
			"id": 2,
			"comment_text": "This is a test comment",
			"user": 2,
			"parent": None,
			"child": []
		}
		self.assertEqual(response.data, data)

	def test_response_status_on_patch_request(self):
		post_data = {
			"comment_text": "This comment is patched",
			"user": 2,
			"parent": None,
		}
		response = self.client.patch('/comments/2', data=post_data, content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_response_status_on_patch_request_if_user_does_not_have_permission(self):
		post_data = {
			"comment_text": "This comment is patched",
			"user": 3,
			"parent": None
		}
		response = self.client.patch('/comments/2', data=post_data, content_type='application/json')
		self.assertEqual(response.status_code, 403)

	def test_response_status_on_delete_request_if_user_does_not_have_permission(self):
		post_data = {
			"user": 3,
		}
		response = self.client.delete('/comments/2', data=post_data, content_type='application/json')
		self.assertEqual(response.status_code, 403)
	
	def test_response_status_on_delete_request(self):
		post_data = {
			"user": 2,
		}
		response = self.client.delete('/comments/2', data=post_data, content_type='application/json')
		self.assertEqual(response.status_code, 204)
