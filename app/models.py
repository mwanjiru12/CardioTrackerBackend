from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import db
from datetime import datetime
from sqlalchemy import Date
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=True)

class ActiveDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)
    streak = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='active_days')

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active_day_id = db.Column(db.Integer, db.ForeignKey('active_day.id'), nullable=False)
    exercise_type = db.Column(db.String(50), nullable=False)
    activity_length = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    summary = db.Column(db.String(250), nullable=True)
