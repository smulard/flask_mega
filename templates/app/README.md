**"A Hello, World" Flask Application**

The application will exist in a _package_. In Pythonm a sub-directory for that includes a `__init__.py` file is considered a package, and can be imported.
When you import a package, the `__init__.py` executes and defines what symbols the package exposes to the outside world.

The package `app` will host the application. 

Before running, the `FLASK_APP` environmental  variable must be set:

```$ export FLASK_APP=microblog.py```

To run the web application" ```$ flask run```