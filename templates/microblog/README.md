# Templates
For now, the application only has a templorary user 'Miguel'. The application has a heading that welcomes the user.

Instead of returning a simple string, the view function in the application will now return an HTML page.

#### Template Inheritance
Most web applications have a navigation bar at the top of the page with a few frequency used links, such as a link to edit your profile, to login, logout, etc.
Instead of putting the navigation bar in the `index.html` template with some more HTML,
Jinja2 has a template inheritance feature that specifically addresses this problem.
It allows  the parts of the page layout that are common to all templates to a base template, from which all ofther templates are dervied.

The `base.html` file is a base template that includes a simple navigation bar and also the title logic.
