from flask import request, jsonify
from app import db  # Assuming your main file is named app.py
from models import Episode, Guest, Appearance

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    else:
        return jsonify({"error": "Episode not found"}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except Exception:
        return jsonify({"errors": ["validation errors"]}), 400
