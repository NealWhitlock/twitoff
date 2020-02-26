"""Code for our app. The main application."""

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user

# Make our app factory
def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # Stop tracking modifications on SQLAlchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    
    @app.route('/user', methods=['POST', 'GET'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        # import pdb; pdb.set_trace()
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = "Error adding {}: {}".format(name,e)
            tweets = []
        return render_template('user.html', title=name, 
                               tweets=tweets, message=message)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset', users=[])

    return app
