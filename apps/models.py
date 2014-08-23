"""
models.py

"""
from apps import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    fb_id = db.Column(db.String(255), unique=True)
    img_url = db.Column(db.Text())
    date_created = db.Column(db.DateTime())


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref('group', cascade='all, delete-orphan', lazy='dynamic'))
    date_created = db.Column(db.DateTime())


class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    description = db.Column(db.Text())
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', backref=db.backref('quest', cascade='all, delete-orphan', lazy='dynamic'))
    date_created = db.Column(db.DateTime())
    date_expired = db.Column(db.DateTime())
    success = db.Column(db.Integer, default=0)


class Groupmember(db.Model):
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    group = db.relationship('Group', backref=db.backref('groupmember', cascade='all, delete-orphan', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('groupmember', cascade='all, delete-orphan', lazy='dynamic'))


class Questmember(db.Model):
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'), primary_key=True)
    quest = db.relationship('Quest', backref=db.backref('questmember', cascade='all, delete-orphan', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('questmember', cascade='all, delete-orphan', lazy='dynamic'))


