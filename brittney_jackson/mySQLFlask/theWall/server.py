from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5

app = Flask(__name__)
app.secret_key = 'OopsOneMoreTime'

mysql = MySQLConnector(app,'wall')

def registrationVal(form_data):
    errors = False

    if len(request.form['first_name']) <2:
        flash('First name cannot be empty')
        errors = True

    if len(request.form['last_name']) <2:
        flash('Last name cannot be empty')
        errors = True

    if len(request.form['email']) <1:
        flash('Email cannot be empty')
        errors = True

    if len(request.form['password']) <1:
        flash('Password cannot be empty')
        errors = True

    if request.form['passwordC'] != request.form['password']:
        flash('passwords must match')
        errors = True
    print errors
    return errors    

@app.route('/')
def index():                         
    return render_template('index.html') 

@app.route('/register', methods=['POST'])
def register():

    errors = registrationVal(request.form)

    if errors == True:
        return redirect('/')
    else:
        h_pw = md5.new(request.form['password']).hexdigest()

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name': request.form['last_name'],
                 'email': request.form['email'],
                 'password': h_pw,
               }
        flash('Successful Registration. Please Login Below.')
        print 'got all the information'
        mysql.query_db(query, data)
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
    data = { 'email': email, 'password': password }
    user = mysql.query_db(query, data)
    session['name'] = user[0]['first_name']
    

    print session['name']

    if user != []:
        print 'hello'
        session['userid'] = user[0]['id']
        return redirect('/wall')
    else:
        flash('Oh No Big Fella. What is you doin?')
        return redirect ('/')

@app.route('/wall')
def wall():
    return render_template('wall.html')

@app.route('/message', methods=['POST'])
def message():
    query = "INSERT INTO messages (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(),:userid )"
    data = {
            'userid': session['userid'],
            'message': request.form['message'],
            }

    
    print 'got your message'
    mysql.query_db(query, data)

    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    query = "INSERT INTO comments (comment, created_at, updated_at, users_id) VALUES (:comment, NOW(), NOW(), :userid)"
    data = {
            'userid': session['userid'],
            'comment': request.form['comment'],
            }

    print 'got your comment'
    mysql.query_db(query, data)


    return redirect('/wall')



    
app.run(debug=True)
