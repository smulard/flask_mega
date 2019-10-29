'''
The app package is defined by the app directory and the __init__.py script. It's references in the 'from app import routes' statement.
The 'app' variable is defined as a instance of class 'Flask' in the '__init__.py' script, which makes it a member of the 'app' package.
The routes are the different URLs that the application implements. In Flask,, handlers for the application routes are written as Python functions,
called 'view functions'. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requents a given URL.
'''
'''Explanation:
The view function just returns a greeting as a string. The two '@app.route' lines above the function are 'decorators'.
Decorators are a unique feature of Python. A decorator modifies the function that follows it.
A common pattern with decorators is to use them to register functions as callbacks for certain events. In this case, 
'@app.route' decorator creates an association between the URL given as an argument and the function.
In this example there are two decorators, which associate the URLs '/' and '/index' to this function.
This means that when a web browser requests either of these two URLS, Flask is going to invoke this function
and pass the return value of it back to the browser as a response.
'''
from flask import render_template, flash, redirect #invokes Jinja2 tempslate
from app import app
from app.forms import LoginForm #import LoginForm from forms.py

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'} #mock user
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm() #instantiates LoginForms object
    """ When browser sends the GET request for the web page with the form, validate_on_submit returns false,
    which would skip the if statement and renders the template in the last line of the function.
    """
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
           form.username.data, form.remember_me.data)) #flash shows message to user, it stores the message
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form=form) #send LoginForms as a template