"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify
import os
import time
import uuid
from app import db
from app.models import UserProfile
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/profile', methods=['GET','POST'])
def profile():
    file_folder = app.config['UPLOAD_FOLDER']

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        age = request.form['age']
        biography = request.form['biography']

        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(file_folder, filename))

        gender = request.form['gender']
        date = time.strftime("%Y/%b/%d")
        userid = str(uuid.uuid4().fields[-1])[:8]
       
        flash('profile saved')

        user = UserProfile(id=userid, date=date, first_name=first_name, last_name=last_name,
        username=username, age=age, biography=biography, gender=gender, image=file.filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    """Render the website's profile page."""
    return render_template('profile.html')

@app.route('/profiles', methods=['GET','POST'])
def profiles():
    all_users=[]
    users = UserProfile.query.filter_by().all()
    print users
    if request.method == 'POST':
        for user in users:
            all_users += [{'username':user.username, 'userid':user.id}]
        return jsonify(users=all_users)
    elif request.method == 'GET':
        return render_template('profiles.html', profiles=users)
    

@app.route('/profile/<userid>', methods=['GET','POST'])
def profileid(userid):
    id = userid
    userdb={}
    
    user = UserProfile.query.filter_by(id=id).first()
    print user
    if request.method == 'POST':
        userdb={'userid':user.id, 'username':user.username, 'profile_image':user.image, 
        'gender':user.gender, 'age':user.age, 'created_on':user.date}
        return jsonify(userdb)

    elif request.method == 'GET' and user:
        return render_template('profile_for_oneUser.html', profile=user)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")