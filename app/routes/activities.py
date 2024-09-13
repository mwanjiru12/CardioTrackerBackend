from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Activity, ActiveDay
from .. import db

bp = Blueprint('activities', __name__)

@bp.route('/activities', methods=['GET'])
@jwt_required()
def get_activities():
    activities = Activity.query.all()
    result = [{
        'id': activity.id,
        'active_day_id': activity.active_day_id,
        'exercise_type': activity.exercise_type,
        'activity_length': activity.activity_length,
        'calories': activity.calories,
        'distance': activity.distance,
        'rating': activity.rating,
        'summary': activity.summary
    } for activity in activities]
    return jsonify(result)

@bp.route('/activities/<int:id>', methods=['GET'])
@jwt_required()
def get_activity(id):
    activity = Activity.query.get(id)
    if activity:
        return jsonify({
            'id': activity.id,
            'active_day_id': activity.active_day_id,
            'exercise_type': activity.exercise_type,
            'activity_length': activity.activity_length,
            'calories': activity.calories,
            'distance': activity.distance,
            'rating': activity.rating,
            'summary': activity.summary
        })
    return jsonify({'message': 'Activity not found'}), 404

@bp.route('/activities', methods=['POST'])
@jwt_required()
def create_activity():
    data = request.json
    new_activity = Activity(
        active_day_id=data.get('active_day_id'),
        exercise_type=data.get('exercise_type'),
        activity_length=data.get('activity_length'),
        calories=data.get('calories'),
        distance=data.get('distance'),
        rating=data.get('rating'),
        summary=data.get('summary')
    )
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({
        'id': new_activity.id,
        'active_day_id': new_activity.active_day_id,
        'exercise_type': new_activity.exercise_type,
        'activity_length': new_activity.activity_length,
        'calories': new_activity.calories,
        'distance': new_activity.distance,
        'rating': new_activity.rating,
        'summary': new_activity.summary
    }), 201

@bp.route('/activities/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_activity(id):
    activity = Activity.query.get(id)
    if activity:
        db.session.delete(activity)
        db.session.commit()
        return jsonify({'message': 'Activity deleted successfully'})
    return jsonify({'message': 'Activity not found'}), 404

@bp.route('/active_days/<int:id>/activities', methods=['GET'])
@jwt_required()
def get_activities_by_active_day(id):
    activities = Activity.query.filter_by(active_day_id=id).all()
    result = [{
        'id': activity.id,
        'active_day_id': activity.active_day_id,
        'exercise_type': activity.exercise_type,
        'activity_length': activity.activity_length,
        'calories': activity.calories,
        'distance': activity.distance,
        'rating': activity.rating,
        'summary': activity.summary
    } for activity in activities]
    return jsonify(result)

@bp.route('/activities/<string:exercise_type>/top/<string:column>', methods=['GET'])
@jwt_required()
def get_top_activity(exercise_type, column):
    valid_columns = ['activity_length', 'calories', 'distance', 'rating']
    if column not in valid_columns:
        return jsonify({'message': 'Invalid column parameter'}), 400

    top_activity = Activity.query.filter_by(exercise_type=exercise_type).order_by(getattr(Activity, column).desc()).first()
    if top_activity:
        active_day = ActiveDay.query.get(top_activity.active_day_id)
        return jsonify({
            'id': top_activity.id,
            'active_day_id': top_activity.active_day_id,
            'exercise_type': top_activity.exercise_type,
            'activity_length': top_activity.activity_length,
            'calories': top_activity.calories,
            'distance': top_activity.distance,
            'rating': top_activity.rating,
            'summary': top_activity.summary,
            'active_day': {
                'id': active_day.id,
                'date': active_day.date,
                'day_of_week': active_day.day_of_week,
                'streak': active_day.streak,
                'user_id': active_day.user_id
            }
        })
    return jsonify({'message': 'No activities found for this type'}), 404
