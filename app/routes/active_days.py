from flask import Blueprint, request, jsonify
from app.models import ActiveDay, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime



bp = Blueprint('active_days', __name__)

@bp.route('/active_days', methods=['POST'])
@jwt_required()
def add_active_day():
    user_id = get_jwt_identity()
    data = request.json

    # Convert date string to datetime object
    date_str = data.get('date')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    day_of_week = data.get('day_of_week')
    streak = data.get('streak', 1)  # Default to 1 if not provided

    # Create a new active day
    new_active_day = ActiveDay(
        date=date,
        day_of_week=day_of_week,
        streak=streak,
        user_id=user_id
    )

    try:
        db.session.add(new_active_day)
        db.session.commit()
        return jsonify({'message': 'Active day added successfully'}), 201
    except Exception as e:
        print("Error adding active day:", str(e))
        return jsonify({'message': 'Error adding active day'}), 500

@bp.route('/active_days', methods=['GET'])
@jwt_required()
def get_active_days():
    user_id = get_jwt_identity()
    active_days = ActiveDay.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': day.id, 'date': day.date, 'day_of_week': day.day_of_week, 'streak': day.streak
    } for day in active_days])

@bp.route('/active_days/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_active_day(id):
    day = ActiveDay.query.get(id)
    if day:
        db.session.delete(day)
        db.session.commit()
        return jsonify({'message': 'Deleted successfully'})
    return jsonify({'message': 'Not found'}), 404

@bp.route('/active_days/<int:id>', methods=['GET'])
@jwt_required()
def get_active_day(id):
    # Query the database for the active day by ID
    active_day = ActiveDay.query.get(id)

    if not active_day:
        return jsonify({'message': 'Active day not found.'}), 404

    # Return the active day details
    return jsonify({
        'active_day': {
            'id': active_day.id,
            'date': active_day.date,
            'day_of_week': active_day.day_of_week,
            'streak': active_day.streak,
            'user_id': active_day.user_id
        }
    }), 200