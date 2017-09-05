'''adding posts for particular user'''
from app import db,models
import datetime
u = models.User.query.get(1)
p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()