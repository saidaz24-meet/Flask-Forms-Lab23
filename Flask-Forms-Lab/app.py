from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)



facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]
users = {"said":"said123","yahli":"321","yazan":"damn","guy":"very_magical"}
userFriends = {"said":["a","b","c", "d", "e", "f"],
"yahli":["f","h","no", "yes", "mabye", "sure"],
"yazan":["me","him","her", "they", "no", "zero"],
"guy":["wow","ahmad","rami", "no friends", "empty", "for run"]}
@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
		if request.method == 'GET':
			return render_template('login.html')

		else :
			if request.form['username'].lower() in users and request.form['password']==users[request.form['username'].lower()]:
				return redirect(url_for('home', name = request.form['username']))
			else :
				return render_template('login.html')
  
@app.route('/home/<string:name>')
def home(name):
	return render_template('home.html',friends = facebook_friends,userFr = userFriends, user = name)


@app.route('/friend_exists/<string:name>',methods=['GET', 'POST'])
def friend_exists(name):
	check = False
	if name in facebook_friends :
		check = True
	return render_template('friend_exists.html',in_it = check,n = name)
	


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
