# TASK AND GOAL MANAGER
#### CS50x Final Project Author: Bryan Lim
#### Note: Duplicated copy (25/02/2025)
#### Description:

##### Overview:
For my CS50x final project, I coded a simple Task and Goal Manager web application. The aim of this application is to help users record and organise day to day tasks, as well as systematically record and track long term goals. This application uses Python, Javascript, CSS, HTML, Flask, SQLite3, and Jinja2.

##### what each file contains and does:
My project consists of a "static" directory, a "flask_session" directory, a "templates" directory, an app.py file, and afew micellaneous files, .

##### static directory:
The static directory contains the file which stores the background picture displayed across the entire application. It also contains styles.css and the js directory, used to contain javascript to make the elements on the static pages responsive.

##### flask session directory:
Since this application uses an account log-in log-out mechanism, flask session helps to contain all sessions in seperate files.

##### app.py:
app.py is central to this flask application, handling all routes, calculations, data processing, data updating, and data retrieving. It connects the frontend html pages and the backend sqlite3 database, allowing transfer of data from user input to database and vice versa.

##### micellaneous files:
helpers.py defines some functions used in app.py, for example, the apology function, which helps to render pages with fixed text formats across it.
requirements.txt allows the application to run by listing all the dependencies required. users.db serves as the backend database to store all frontend user input.

##### templates directory:
The templates directory contains all the html files.

###### pre_layout.html:
pre_layout.html abstracts away basic html formatting and page layout from register.html and login.html, serving as a template for page-specific html.

###### register.html:
register.html renders a user register page, requiring that the user input a unique username, password, and name for rendering on the pages. If valid, username and password is stored in sqlite3 database through app.py. Passwords are hashed before storing, for security.

###### login.html:
login.html renders a login page, requiring that the user enters their username and password correctly before other pages(files) may be accessed. Username and password is proofread against the sqlite3 database in app.py.

###### layout.html:
layout.html abstracts away basic html formatting and page layout from the rest of the html pages except category_page.html, serving as a template for page-specific html. The difference with pre_layout.html is that layout.html renders the users name, which is collected in the register page. app.py passes this name data to layout.html, enabling the rendering.

###### pre_apology.html and post_apology.html:
These apology pages are rendered when user input is unaccepted. These apology pages also produces varying error texts. For example, in the register page, if the user inputs a username that is already taken, the page returns "username already exists". This is allowed by the apology function defined in helpers.py. The difference between pre_apology.html and apology.html is similar to that of pre_layout.html and layout.html, where pre_apology.html is rendered before user inputs their name. Both these apology pages provide a "back to homepage button."

###### home.html:
home.html is the main page of this web application. It contains a navigation bar with all the users categories, as well as the "add category", "log out" and "change password" buttons. The "add category" button runs the dynamic category_page.html page via app.py (to be explained later). The "log out" button logs the user out. The "change password" button allows the user to change their passwords.

###### password.html and passworded.html:
These pages render the change password screen before and after submitting, allowing the user to change passwords.

###### add_category.html:
add_categories.html renders a page which allows the user to add an element(category) to the navigation bar in home.html. The input is validated by app.py, which prevents duplicate entries.

###### category_page.html:
category_page.html is generated dynamically by app.py every time a new category is added in the homepage (home.html). Every element in the navigation bar, when clicked, generates a new html page. when any of these elements in the navbar are clicked, app.py filters the data in sqlite3, passing the category name and category-specific relevant data into the generated category_page.html. The category name and rows of category data are rendered in the catgeory page with the help of jinja2. Each category page has a back to homepage button, as well as a table with the coloumn headers "goal", "due date", "importance", "remarks", and "status". Rows with status marked as done sink to the bottom of the table, while those marked as "havent started" or "in progress" get pioritised at the top. This allows the user to look back on past completed entries, as well as focus on uncompleted tasks and goals.

###### add_row.html:
add_row.html renders a page that allows the user to add an entry to the goals table in the category page. add_row.html can be rendered by pressing the plus button at the bottom right of the categories page. Javascript also allows for deletion of the elements(category) from the navigation bar.
