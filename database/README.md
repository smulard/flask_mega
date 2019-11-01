#Database

This application is using `Flask-SQLAlchemy`, which is a Flask-friendly wrapper for `SQLAlchemy`, which is an Object Relational Matcher (ORM).
This allows for the ORM to translate high-level operations, like classes, objects and methods into tables and SQL.
Flask-Migrate is also used, which is a Flask wrapper for Alembic, which is a data migration framework for SQLAlchemy.
SQLite is the database being used.

The SQLite is represented by the _database instance_. The database migration engine also has a an instance.
`models.py` defines the initial database schema. When the database changes
Alembic (the migration framework user by Flask-Migrate) will make thse schema changes
in a way that does ot require the database to be recreated from scratch.
Alembic maintains a _migration repository_, which is a directory in which it stores its migration scripts.
Each times a change is made to the database schema, a migration script 
is added to the repository with the details of the change. To apply the migrations to a database, 
these migration scripts are executes in the sequence they were created.

Flask-Migrate exposes its commands through the `flask` command.
The `flask db` sub-command is added by the Flask-Migrate to manage everything
related to database migrations.

Database migrations can either be created automatically or manually.
To generate a migration automatically, Alembic compares the database schema
as defined by the database models, against the actual database schema currently used in the database.
It then populates the migration script with the changes necessary to make the database schema match the
application models. The `flask db migrate` sub-command generates these automatic migrations.

The `flask db migrate` command does make any changes to the database, it just
generates the migration script. To apply changes to the database, the `flask db upgrade` applies
the migration, and the `flask db downgrade` function removes to migration. After migration,
_app.db_ is created, which is the SQLite database. When using MySQL and PostgreSQL, the database must
be created in the database server before running `upgrade`.



### To run the application
The application will exist in a _package_. In Pythonm a sub-directory for that includes a `__init__.py` file is considered a package, and can be imported.
When you import a package, the `__init__.py` executes and defines what symbols the package exposes to the outside world.

The package `app` will host the application.

Before running, the `FLASK_APP` environmental  variable must be set:

```$ export FLASK_APP=microblog.py```

To run the web application ```$ flask run```

To initiate database migrations: ```flask db init```
This creates a "migrations" directory, from Flask-Migrate.

## Other Parts of the Application

#### Web-Forms

This feature is address how to accept input from users through web forms. Web forms are one of the most basic building blocks in any web application.
The forms will allow users to submit blog posts and also for logging into the the application.

For this web-form, the Flask-WTF extension is used, which is a thin weapper around the WTForms package that nicely integrates it with Flask.

The Flask-WTF  extension uses Python classes to represent web forms. A form class simply defines the fields of the form as class variables.
The file, app/forms.py module stores the web form classes. It defines a user login form, which asks the user to enter a username and a password.
It also uncludes a "remember me" check box, and a submit button.
