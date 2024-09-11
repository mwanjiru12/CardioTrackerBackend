from app import create_app, db
from app.models import User, ActiveDay, Activity
from datetime import datetime

def seed_database():
    # Create app and initialize database
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()

        # Create user
        user = User(username='testuser', password='password123', name='Test User', location='Test Location')
        db.session.add(user)
        db.session.commit()

        # Create active days
        active_day1 = ActiveDay(date=datetime(2024, 9, 1), day_of_week='Monday', streak=1, user_id=user.id)
        active_day2 = ActiveDay(date=datetime(2024, 9, 2), day_of_week='Tuesday', streak=2, user_id=user.id)
        db.session.add_all([active_day1, active_day2])
        db.session.commit()

        # Create activities
        activity1 = Activity(active_day_id=active_day1.id, exercise_type='Running', activity_length=30.0, calories=300.0, distance=5.0, rating=4, summary='Morning run')
        activity2 = Activity(active_day_id=active_day2.id, exercise_type='Cycling', activity_length=45.0, calories=500.0, distance=15.0, rating=5, summary='Evening bike ride')
        db.session.add_all([activity1, activity2])
        db.session.commit()

if __name__ == '__main__':
    seed_database()
