# -*- coding: utf-8 -*-
#
# authors: Vipin
#
# Created on Tue June 5 2019

# -- Local Libraries
from .models import Comment
from .serializers import CommentSerializer
from .serializers import GetCommentSerializer

# -- External Libraries
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer


class CommentDetail(APIView):
    """
    Retrieve, update or delete a comment instance.
    """
    def get_object(self, pk):
        """
        :params self
        :params pk
        :return: Comment object or Http404
        """
        
        try:
            # Return the Comment object fetched using the primary key
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            # If the comment is not found, return Http404
            raise Http404

    def get(self, request, pk, format=None):
        """
        :params self
        :params request
        :params pk
        :return: Serialized comment and all it's replies
        """
        
        comment = self.get_object(pk)
        
        # Serialize comments data and all it's replies
        serializer = GetCommentSerializer(comment)
        
        # Return serialized data
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        """
        :params self
        :params request
        :params pk
        :return: Serialized comment and all it's replies after saving the uodated object
        """

        comment = self.get_object(pk)

        # Serialize the data received with the request
        serializer = CommentSerializer(comment, data=request.data)
        
        # If serializer is valid, save the Comment instance with the updated data
        if serializer.is_valid():

            # Check if the user has the permission to edit this comment
            if comment.has_permission(serializer.validated_data.get('user').id):
                # Save the updated data
                serializer.save()
                return Response(serializer.data)
            else:
                # Send 403 response code and an appropriate response message
                response = {
                    "error": "This user is not authorized to edit this comment"
                }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        
        # If not valid, return the appropriate response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        :params self
        :params request
        :params pk
        :return: Return HTTP_204_NO_CONTENT as the status code after the object is deleted
        """
        comment = self.get_object(pk)
        
        # Check if the user requesting to delete the comment is the same as the user who created it
        if comment.has_permission(request.data.get('user')):
            # Delete the comment
            comment.delete()

            # Return appropriate response
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            response = {
                "error": "This user is not authorized to delete this comment"
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
