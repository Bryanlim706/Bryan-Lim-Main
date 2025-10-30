# TASK AND GOAL MANAGER
#### CS50x Final Project Author: Bryan Lim
#### Description:
##### Overview:
For my CS50x final project, I coded a simple Task and Goal Manager web application. The aim of this application is to help users record and organise day-to-day tasks, as well as systematically track long-term goals. This application uses Python, Javascript, CSS, HTML, Flask, SQLite3, and Jinja2.

##### What each file contains and does:
My project consists of a "static" directory, a "flask_session" directory, a "templates" directory, an app.py file, and a few miscellaneous files.

##### static directory:
The static directory contains the file which stores the background picture displayed across the entire application. It also contains styles.css and the js directory, which holds JavaScript files that make the static page elements responsive.

##### flask_session directory:
Since this application uses an account log-in log-out mechanism, Flask-Session stores all user sessions in separate files.

##### app.py:
app.py is central to this Flask application, handling all routes, calculations, data processing, updates, and data retrieval. It connects the frontend HTML pages and the backend SQLite3 database, allowing data to flow between user inputs and the database.

##### miscellaneous files:
helpers.py defines several functions used in app.py, such as the apology function, which renders pages with consistent text formats.
requirements.txt lists all dependencies required for the application to run. users.db serves as the backend database to store all user input from the frontend.

##### templates directory:
The templates directory contains all the HTML files.

###### pre_layout.html:
pre_layout.html abstracts common HTML formatting and page structure from register.html and login.html, serving as their base template.

###### register.html:
register.html renders a user register page, requiring the user to input a unique username, password, and display name for rendering on the pages. If valid, the username and hashed password are stored in the SQLite3 database via app.py.

###### login.html:
login.html renders a login page, requiring that the user enters their username and password correctly before other pages(files) may be accessed. The username and password are verified against the SQLite3 database through app.py.

###### layout.html:
layout.html abstracts away basic HTML formatting and page layout from the rest of the HTML pages (except category_page.html), serving as a template for page-specific HTML. The difference from pre_layout.html is that layout.html also renders the user’s name, which is collected in the register page. app.py passes this name data to layout.html for rendering.

###### pre_apology.html and post_apology.html:
These apology pages are rendered when user input is invalid or unaccepted. These apology pages also produce varying error messages. For example, in the register page, if the user inputs a username that is already taken, the page returns "username already exists". This is allowed by the apology function defined in helpers.py. The difference between pre_apology.html and apology.html is similar to that of pre_layout.html and layout.html, where pre_apology.html is rendered before user inputs their name. Both pages provide a “Back to Homepage” button.

###### home.html:
home.html is the main page of this web application. It contains a navigation bar listing all user categories, as well as “Add Category”, “Log Out”, and “Change Password” buttons. The "add category" button runs the dynamic category_page.html page via app.py (to be explained later). The "log out" button logs the user out. The "change password" button allows the user to change their passwords.

###### password.html and passworded.html:
These pages render the Change Password screen before and after submitting, allowing the user to change passwords.

###### add_category.html:
add_category.html renders a page that allows the user to add a new category to the navigation bar on home.html. The input is validated by app.py, which prevents duplicate entries.

###### category_page.html:
category_page.html is generated dynamically by app.py every time a new category is added on the homepage (home.html). Each element in the navigation bar, when clicked, generates a new HTML page. When clicked, app.py filters the data in SQLite3, passing the category name and relevant data into the generated category_page.html. The category name and rows of category data are rendered in the category page with the help of Jinja2. Each category page has a back to homepage button, as well as a table with the column headers "Goal", "Due Date", "Importance", "Remarks", and "Status". Rows marked as “Done” are moved to the bottom of the table, while those marked as “Haven’t Started” or “In Progress” are prioritised at the top. This allows the user to look back on past completed entries, as well as focus on uncompleted tasks and goals.

###### add_row.html:
add_row.html renders a page that allows the user to add an entry to the goals table in the category page. add_row.html can be rendered by pressing the plus button at the bottom right of the categories page. JavaScript also enables users to delete categories from the navigation bar.

---

#### How to run this application:
1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/<your-repository-name>.git
   cd <your-repository-name>/task_and_goal_manager

2. Set up a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate     # On macOS/Linux
   venv\Scripts\activate        # On Windows

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Set environment variables
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development   # Optional: enables debug mode

5. Run the Flask server
   ```bash
   flask run

6. Access the app
Open your web browser and go to:
   ```bash
   http://127.0.0.1:5000

---

#### Note: This is a duplicated copy (25/02/2025)

Thank you for reviewing my project!

Bryan Lim
