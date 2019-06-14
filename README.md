# Commenting System

This is a commenting system where users can add comments and replies to comments. The users can also add replies to replies.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See **Deployment** for notes on how to use the already deployed live system.

* Clone the repository on your local machine by using the command:

```
$ git clone https://github.com/vipingup17/commenting-system.git
```

### Prerequisites

* You will require Python 3.x as Django 2.x is being used and postgresql 10.x and above

### Installing

* Create and activate a virtual environment and install all project dependencies

```
	$ cd commenting-system
	$ pip install -r requirements.txt
```

* Create a Postgresql database configure the database settings as per your local database engine and credentials (See settings.py)

## Running the tests

I have written unit tests for this system. The unit tests are written in test_views.py file of comments app

Run the following command to run the unit tests

```
python manage.py test
```

### Running the project on local machine

* If there is no unit test that fails, go ahead and run the django development server on port 8000 by executing the following command:

```
python manage.py runserver
```

## Using the application

To use the application

Let us say you have created 4 users for working with the API endpoints

```
User2 with pk as 2
User3 with pk as 3
User4 with pk as 4
User5 with pk as 5
```

Please find below the API endpoints used to perform operations on comments

API endpoint for creating a comment or a reply:

```
http://localhost:8000/comments/create
```

To create a new comment or a reply, send the following sample data in the body of the HTTP POST request

```
{
	"comment_text": "This is a sample comment",
	"user": 3,
	"parent": null

}
```

The above API call should get back a response such as follows:

```
{
    "id": 7,
    "comment_text": "This is a sample comment",
    "user": 3,
    "parent": null
}
```
where id will be the primary key of the newly created comment

To create a reply (which is also a comment), the parent paramter will have an id corresponding to the comment for which this reply is being written

```
{
	"comment_text": "This is a sample reply",
	"user": 3,
	"parent": 7

}
```

In the above example, 3 is the primary key or id of the user. 'parent' will be null for a comment and an integer for a reply (integer will be the primary key of the comment for which the reply is getting created)  

API endpoint for get, edit, delete operations on a comment:

```
http://localhost:8000/comments/pk
```
where pk is the primary key of a comment or a reply

To fetch a comment and all of it's replies, send an HTTP GET request on the above URL with pk as an integer (the primary key of the comment)

To edit a comment, send an HTTP PATCH request on the above URL with a sample body as follows:

* Suppose you want to edit a comment with id as 5, then your URL will be http://localhost:8000/comments/5 and the body will be as follows:

```
{
	"comment_text": "This is a sample comment text for editing an already existing comment",
	"user": 2,
	"parent": null
}
```

If the user is the one that created the comment, the comment will get updated otherwise an error message is sent in response along with 403 status code

To delete a comment, send an HTTP DELETE request on the above URL with pk as an integer (the primary key of the comment). 

In the body of the message, send the user id as follows:

```
{
	"user": 2
}
```
If the user is the one that created the comment, the comment will get deleted otherwise an error message is sent in response along with 403 status code
