from app import db, models
u1 = models.User(name='john', email='john@email.com')
db.session.add(u1)
db.session.commit()
u2 = models.User(name='susan', email='susan@email.com')
db.session.add(u2)
db.session.commit()
print("finished adding data")