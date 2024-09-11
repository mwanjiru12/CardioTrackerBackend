from flask import Blueprint, request, jsonify
from app.models import ActiveDay, db
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('active_days', __name__)

@bp.route('/active_days', methods=['POST'])
@jwt_required()
def add_active_day():
    user_id = get_jwt_identity()
    data = request.json
    new_day = ActiveDay(date=data['date'], day_of_week=data['day_of_week'], streak=data['streak'], user_id=user_id)
    db.session.add(new_day)
    db.session.commit()
    return jsonify({'active_day': new_day.id}), 201

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
