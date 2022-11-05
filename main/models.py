from django.db import models
from sqlalchemy import false

class User(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Orders(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    price = models.CharField(max_length=30)
    note = models.CharField(max_length=500)
    def __str__(self):
        return self.customer_id
    
class Blog(models.Model):
    # """Blog Post"""
    title=models.CharField(max_length=100, null=false)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    description = models.CharField(max_length=500,null=True)
    content=models.TextField()
    date =models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    #  """ comment"""
    id_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=500,null=false)
    date = models.DateTimeField(auto_now_add=True)
    