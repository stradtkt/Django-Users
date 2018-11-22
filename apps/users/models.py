from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date


class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be 2 or more characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be 2 or more characters"
        if len(postData['first_name']) > 30:
            errors['first_name'] = "First name needs to be less then 30 characters"
        if len(postData['last_name']) > 30:
            errors['last_name'] = "Last name needs to be less then 30 characters"
        if not postData['first_name'].isalpha():
            errors['first_name'] = "First name needs to be only letters"
        if not postData['last_name'].isalpha():
            errors['last_name'] = "Last name needs to be only letters"

        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"
        try:
            postData['username']
        except ValidationError:
            errors['username'] = "Your username is not valid"
        else:
            if User.objects.filter(username=postData['username']):
                errors['username'] = "This username already exists"


        if len(postData['password']) < 4:
            errors['password'] = "Please enter a longer password, needs to be four or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class MessageManager(models.Manager):
    def validate_message(self, postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "You need to have a longer message with 5 or more characters"
        if len(postData['content']) > 1000:
            errors['content'] = "Your message needs to be smaller tham 1000 characters"
        return errors

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def validate_comment(self, postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "You need to have a longer message with 5 or more characters"
        if len(postData['content']) > 1000:
            errors['content'] = "Your message needs to be smaller tham 1000 characters"
        return errors

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name='message', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()