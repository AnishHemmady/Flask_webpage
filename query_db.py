'''querying_database'''
from app import models,db

user = models.User.query.get(1)
posts=user.posts.all()
print(user)
print(posts)

