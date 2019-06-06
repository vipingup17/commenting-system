# Commenting System

This is a commenting system where users can add comments and replies to comments. The users can also add replies to replies.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to use the already deployed live system.

* Clone the repository on your local machine by using the command:
```
$ git clone https://github.com/vipingup17/commenting-system.git
```

### Prerequisites

* You will need python 3.x as Django 2.x is being used and postgresql 10.x and above

### Installing

* Create and activate a virtual environment and install all project dependencies

```
	$ cd commenting-system
	$ pip install -r requirements.txt
```

* Configure the database settings as per your local database engine and credentials (See settings.py)
* Run the django development server on port 8000

## Deployment

To use the already deployed system

* The system is deployed on AWS EC2 having Ubuntu 18.04
* Gunicorn and Nginx are used as application and web servers respectively

I have created 4 users for working with the API endpoints

User2 with pk as 2
User3 with pk as 3
User4 with pk as 4
User5 with pk as 5

Please find below the API endpoints used to perform operations on comments

API endpoint for creating a comment or a reply:

```
http://3.15.40.213/comments/create
```

To create a new comment or a reply, send the following sample data in the body of the POST request

```
{
	"comment_text": "This is a sample comment",
	"user": 3,
	"parent": null

}
```

To create a reply (which is also a comment), the parent paramter will have an id corresponding to the comment for which this reply is being written

```
{
	"comment_text": "This is a sample comment",
	"user": 3,
	"parent": 1

}
```

In the above example, 3 is the primary key or id of the user. 'parent' will be null for a comment and an integer for a reply(integer will the primary key of the comment for which the reply is getting created)  

API endpoint for get, edit, delete operations on a comment:

```
http://3.15.40.213/comments/pk
```
where pk is the primary key of a comment or a reply

To get a comment, send an HTTP GET request on the above URL with pk as an integer (the primary key of the comment)

To delete a comment, send an HTTP DELETE request on the above URL with pk as an integer (the primary key of the comment)

To edit a comment, send an HTTP PATCH request on the above URL with a sample body as follows:

Suppose you want to edit a comment with id as 5, then your URL will be http://3.15.40.213/comments/pk and the body will be as follows:

```
{
	"comment_text": "This is a sample comment text for editing an already existing comment",
	"user": 2,
	"parent": null
}
```
