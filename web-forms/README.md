# Web-Forms

This feature is address how to accept input from users through web forms. Web forms are one of the most basic building blocks in any web application.
The forms will allow users to submit blog posts and also for logging into the the application.

For this web-form, the Flask-WTF extension is used, which is a thin weapper around the WTForms package that nicely integrates it with Flask.

The Flask-WTF  extension uses Python classes to represent web forms. A form class simply defines the fields of the form as class variables.
The file, app/forms.py module stores the web form classes. It defines a user login form, which asks the user to enter a username and a password.
It also uncludes a "remember me" check box, and a submit button.

### To run the application
The application will exist in a _package_. In Pythonm a sub-directory for that includes a `__init__.py` file is considered a package, and can be imported.
When you import a package, the `__init__.py` executes and defines what symbols the package exposes to the outside world.

The package `app` will host the application.

Before running, the `FLASK_APP` environmental  variable must be set:

```$ export FLASK_APP=microblog.py```

To run the web application" ```$ flask run```
