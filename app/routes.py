from app import app, db
from flask import request, jsonify
from app.models import Contact


# set index route to return nothing, just so no error
@app.route('/')
def index():
    return ''


@app.route('/api/save', methods=['GET', 'POST'])
def save():
    try:
        # get headers first
        name = string(request.headers.get('name'))
        email = string(request.headers.get('email'))
        message = string(request.headers.get('message'))

        if not name and not email and not message:
            return jsonify({ 'error': 'please fill out all information' })

        if not isinstance(name, string) and not isinstance(email, string) and not isinstance(message, string):
            return jsonify({ 'error': 'invalid input' })

        # create an event
        contact_msg = Event(name=name, email=email, message=message)

        # add to stage and commit to db
        db.session.add(contact_msg)
        db.session.commit()

        return jsonify({ 'success': 'message sent' })
    except:
        return jsonify({ 'error': 'something went wrong' })
