# Python---Flask-Routes-Introduction
Basic syntax formats of Flask API applications

# Instructions to Run FLASK applications

• Command to create virtual environment For Flask Project
	- Create a folder and insider the folder run Command prompt
	-  py -m venv AnyNameForVirtualEnviroment  - This command Creats a Flask Project inside that folder
	- Type :   "env\Scripts\activate"  - To activate the project
	- Type : pip install flask
	- 

• How To run Flask App
	- Go the folder where "app.py" exists through command prompt.
	- Type :   "env\Scripts\activate"
	- Type:  set FLASK_APP = app.py
	- Type:    flask run  -> Whenever you want to run your App


What is Routes?
	1. Routes refer to URL patterns of an App. ( ex   myapp.com/home).  Through routes only users can consume the APIs that we are developing. 
	- @app.route("/")  is a Python decorator that Flask provides to assign URLs in our app to functions easily.


