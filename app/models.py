from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=True)

    # Optionally, you can add a __repr__ method for better debug output
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

class ActiveDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)
    streak = db.Column(db.Integer, default=1, nullable=False)  # Default value
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='active_days')

    def __repr__(self):
        return f"<ActiveDay(id={self.id}, date={self.date}, streak={self.streak})>"

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active_day_id = db.Column(db.Integer, db.ForeignKey('active_day.id'), nullable=False)
    exercise_type = db.Column(db.String(50), nullable=False)
    activity_length = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    summary = db.Column(db.String(250), nullable=True)
    active_day = db.relationship('ActiveDay', backref='activities')

    def __repr__(self):
        return f"<Activity(id={self.id}, exercise_type={self.exercise_type}, length={self.activity_length})>"