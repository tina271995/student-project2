from config import db,app

class User(db.Model):
    user_id = db.Column('user_id',db.Integer(),primary_key=True)
    firstname = db.Column('firstname', db.String(30))
    lastname = db.Column('lastname', db.String(30))
    email = db.Column('email', db.String(30),unique=True)
    gender = db.Column('gender', db.String(10))
    #address = db.Column('address', db.String(255))

class Credentials(db.Model):
    username = db.Column('username', db.String(30), primary_key = True)
    password = db.Column('password', db.String(255))
    userref = db.Column('u_id', db.ForeignKey('user.user_id'), unique=True)


user_address = db.Table('user_address',
    db.Column('u_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('address_id', db.Integer, db.ForeignKey('address.address_id'), primary_key=True)
)

class Address(db.Model):
    adr_id = db.Column('address_id', db.Integer(), primary_key=True)
    city = db.Column('city', db.String(30))
    state = db.Column('state', db.String(30))
    users = db.relationship('User', secondary=user_address, backref=db.backref('addresses', lazy=True))

class Phone(db.Model):
    phone_num = db.Column('phone_number', db.Integer(), primary_key=True)
    vendor = db.Column('vendor', db.String(30))
    userref = db.Column('u_id', db.ForeignKey('user.user_id'), unique=False)

with app.app_context():
    db.create_all()

