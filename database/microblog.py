'''
Script at the top-level that defines the Flask application instance.
All it does is imports the application instance.
The Falsk application instance is called 'app' and is a memeber of the app package.
The 'from app import app' statement imports the 'app' variable that is a member of the 'app' package.
'''

from app import app
from app.models import User, Post

@app.shell.context_processor #registers the function as a shell context function
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}